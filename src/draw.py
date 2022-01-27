import networkx as nx
import matplotlib.pyplot as plt
import pickle

node_num = 10  # node の数

node = [i for i in range(node_num)]
edge = []

with open("./res/result.txt", "r") as f:
    txt = f.readlines()
    #print(txt)
    
with open("./res/result_nonhub.pkl", "rb") as f:
    non_hub_edge = pickle.load(f)
    #print(non_hub_edge)

hub = [int(txt[0][2]), int(txt[1][2]), int(txt[2][2])]
#for h in hub:
#    for i in range(node_num):
#        if h != i:
#            edge.append((h, i))
#            edge.append((i, h))

for e in non_hub_edge:
    edge.append(e)
print(len(edge))
for h in hub:
    for i in range(node_num):
        if h != i:
            edge.append((h, i))
            edge.append((i, h))

#print(edge)
G = nx.Graph()
G.add_nodes_from(node)
G.add_edges_from(edge)

color = ["b" for _ in range(node_num)]
size = [300 for _ in range(node_num)]
for h in hub:
    color[h] = "r"
    size[h] = 1000

nx.draw_networkx(G, node_color=color, node_size=size)
#plt.savefig("./res/graph.png")
#plt.show()