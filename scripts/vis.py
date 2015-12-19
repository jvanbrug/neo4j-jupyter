from IPython.display import IFrame
import json
import os
import sys
import uuid

def vis_network(nodes, edges, physics=False):
    html = """
    <html>
    <head>
      <script type="text/javascript" src="../lib/vis/dist/vis.js"></script>
      <link href="../lib/vis/dist/vis.css" rel="stylesheet" type="text/css">
    </head>
    <body>

    <div id="{id}"></div>

    <script type="text/javascript">
      var nodes = {nodes};
      var edges = {edges};

      var container = document.getElementById("{id}");
      
      var data = {{
        nodes: nodes,
        edges: edges
      }};
      
      var options = {{
          nodes: {{
              shape: 'dot',
              size: 25,
              font: {{
                  size: 14
              }}
          }},
          edges: {{
              font: {{
                  size: 14,
                  align: 'middle'
              }},
              color: 'gray',
              arrows: {{
                  to: {{enabled: true, scaleFactor: 0.5}}
              }},
              smooth: {{enabled: false}}
          }},
          physics: {{
              enabled: {physics}
          }}
      }};
      
      var network = new vis.Network(container, data, options);

    </script>
    </body>
    </html>
    """

    unique_id = str(uuid.uuid4())
    html = html.format(id=unique_id, nodes=json.dumps(nodes), edges=json.dumps(edges), physics=json.dumps(physics))
    
    filename = "figure/graph-{}.html".format(unique_id)

    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as network_file:
        network_file.write(html)

    return IFrame(filename, width="100%", height="400")

def draw(graph, options, physics=False, limit=100):
    # The options argument should be a dictionary of node labels and property keys; it determines which property 
    # is displayed for the node label. For example, in the movie graph, options = {"Movie": "title", "Person": "name"}.
    # Omitting a node label from the options dict will leave the node unlabeled in the visualization.
    # Setting physics = True makes the nodes bounce around when you touch them!
    query = """
    MATCH n
    OPTIONAL MATCH (n)-[r]->(m)
    RETURN n, r, m 
    LIMIT {limit}
    """

    data = graph.cypher.execute(query, limit=limit)

    nodes = []
    edges = []

    def get_vis_info(node):
        node_label = list(node.labels)[0]
        prop_key = options.get(node_label)
        vis_label = node.properties.get(prop_key, "")
        vis_id = node.ref.split("/")[1]

        title = {}

        for key, value in node.properties.items():
            if sys.version_info <= (3, 0):
                key = key.encode("utf8")
                value = value.encode("utf8")

            title[key] = value

        return {"id": vis_id, "label": vis_label, "group": node_label, "title": repr(title)}

    for row in data:
        source = row[0]
        rel = row[1]
        target = row[2]

        source_info = get_vis_info(source)

        if source_info not in nodes:
            nodes.append(source_info)

        if rel:
            target_info = get_vis_info(target)

            if target_info not in nodes:
                nodes.append(target_info)

            edges.append({"from": source_info["id"], "to": target_info["id"], "label": rel.type})

    return vis_network(nodes, edges, physics=physics)
