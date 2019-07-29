import networkx as nx

G = nx.Graph()
file = open("data/dblp_graph.txt", "r")
for line in file:
    fields = line.split(';')
    G.add_edge(fields[0], fields[1], weight=float(fields[2]))
file.close()
listfile = open("data/authpaper.txt", "r")
for line in listfile:
    fields = line.split(';')
    papers=fields[1].split("||")
    G.add_node(fields[0], paper=papers)
listfile.close()
nx.write_gpickle(G, "data/test.pkl")
