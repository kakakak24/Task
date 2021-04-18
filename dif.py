import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.approximation import clique
from networkx.algorithms.approximation import independent_set
from networkx.algorithms.approximation import vertex_cover
from networkx.algorithms.approximation import dominating_set
from networkx.algorithms import covering
from networkx.algorithms import tournament
from networkx.algorithms.tree import mst
from networkx.algorithms import euler
from networkx.algorithms.connectivity import edge_kcomponents

# G
fin = open('graph', 'r')
mas = [[0] * 3 for i in range(83)]
for i in range(83):
    s = fin.readline()
    k = s.split()
    for j in range(2):
        mas[i][j] = k[j]
    mas[i][2] = int(k[2])
G = nx.Graph()
G.add_weighted_edges_from(mas)



# g) Maximum matching
print("g)", "M =", nx.maximal_matching(G))
print()

# i) Minimum edge cover
print("i)","F =", covering.min_edge_cover(G))
print()


