import networkx as nx
G = nx.Graph()
file=open("coauth-DBLP-full-proj-graph.txt","r")
for line in file:
	fields=line.split(';')
	G.add_edge(fields[0],fields[1],weight=float(fields[2]))
	print(fields[0],fields[1],fields[2])	
file.close()
nx.write_gpickle(G, "test.pkl")
