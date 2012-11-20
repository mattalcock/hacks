import networkx.generators.small as smallgen

g = smallgen.krackhardt_kite_graph()

"""
Some Basic Graph Functions
"""

print g.number_of_edges()
print g.number_of_nodes()
print g.adjaceny_list()
print g.edges()
print { x : g.neighbors(x) for x in g.nodes()}

"""
Traversal Algorithms
"""


"""
Centrality
"""



