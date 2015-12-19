# neo4j-jupyter

A [series of Jupyter notebooks](http://nicolewhite.github.io/neo4j-jupyter/main.html) to help data scientists get started with Python and Neo4j.

## Requirements

The latest versions of all requirements (as of December 19, 2015) are in
`requirements.txt`.
These can be installed with `pip install -r requirements.txt`.

If you only want a subset of this repo's functionality, `pip install` a subset
of the top-level requirements one-by-one.

Top-level requirements (all other requirements are dependencies of these):

* [jupyter](http://jupyter.org/)
* [py2neo](http://py2neo.org/2.0/)
* [ipython-cypher](http://ipython-cypher.readthedocs.org/en/latest/)
* [pandas](http://pandas.pydata.org/)
* [networkx](https://networkx.github.io/)
* [python-igraph](http://igraph.org/)
* [plotly](https://plot.ly/)

For 3D network graphs, you must install
[Graph3d (renamed from iGraph)](https://github.com/nicolewhite/igraph)
separately from here: https://github.com/nicolewhite/igraph

Windows users need to install
[NumPy](http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy) and
[Python-igraph](http://www.lfd.uci.edu/~gohlke/pythonlibs/#python-igraph) from
Christoph Gohlke's Windows Binaries: http://www.lfd.uci.edu/~gohlke/pythonlibs
