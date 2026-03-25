import math
import networkx as nx
import matplotlib.pyplot as plt

# número de vértices
n = int(input("Número de vértices: "))

# matriz de distâncias
dist = []

print("Digite a matriz (use 'inf' para infinito):")

for i in range(n):
    linha = input().split()
    nova_linha = []
    
    for valor in linha:
        if valor == 'inf':
            nova_linha.append(math.inf)
        else:
            nova_linha.append(float(valor))
    
    dist.append(nova_linha)

# Floyd-Warshall
for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

# mostrar matriz final
print("\nMenores distâncias:")
for linha in dist:
    print(linha)


G = nx.DiGraph()

# adiciona arestas
for i in range(n):
    for j in range(n):
        if i != j and dist[i][j] != math.inf:
            G.add_edge(i, j, weight=dist[i][j])

pos = nx.spring_layout(G)

# desenha nós e arestas
nx.draw(G, pos, with_labels=True)

# desenha os pesos
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.show()