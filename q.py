from igraph import *

g = Graph()
f = open("vertex", "r")
for i in f.read().split("\n"):
    g.add_vertex(i)
f.close()
f = open("T", "r")
for i in f.read().split("\n"):
    i = i.split(" ")
    g.add_edge(i[0], i[1])
for i in range(len(g.vs)):
    print(i,":", g.vs[i]["name"], end=", ")
print(g.to_prufer());
