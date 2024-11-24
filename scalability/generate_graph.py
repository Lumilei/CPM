# -*- coding: utf-8 -*-
import networkx as nx
import matplotlib.pyplot as plt
print('Number of node in ER random network is 10000, The probability of connection is 0.05')
NETWORK_SIZE = 10000
p = 0.05
G = nx.erdos_renyi_graph(n = NETWORK_SIZE, p = p)
ps = nx.spring_layout(G)
nx.draw(G,ps,width=0.6,node_size=10)
plt.savefig('fig.png',bbox_inches='tight')

max_len = 0
sum_path_len = 0
for i in sorted(nx.connected_components(G), key = len, reverse = True):
    if(len(i) >= max_len):
        max_len = len(i)
    else:
        max_len = max_len
print("The degree of giant component:" + str(max_len))

if (max_len >= NETWORK_SIZE):
    aspl = nx.average_shortest_path_length(G)
    print("Average path length:" + str(aspl))
else:
    connected = [n for n, d in G.degree() if d > 0]
    Gcc = sorted(nx.connected_components(G), key=len, reverse=True)
    G = G.subgraph(Gcc[0])

print("Average clustering coefficient:" + str(nx.degree_histogram(G)))
print("Degree distribution of giant componernt:" + str(nx.degree_histogram(G)))

degree = nx.degree_histogram(G)
x = range(len(degree))
y = [z / float(sum(degree)) for z in degree]
plt.loglog(x, y, color = "red", linewidth = 2)
plt.savfig('fig.png', bbox_inches = 'tight')
plt.show()