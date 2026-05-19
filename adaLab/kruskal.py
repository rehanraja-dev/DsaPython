graph = [
    [0, 2, 4, 0],
    [2, 0, 1, 7],
    [4, 1, 0, 3],
    [0, 7, 3, 0]
]

V = len(graph)

edges = []

for i in range(V):

    for j in range(i + 1, V):

        if graph[i][j] != 0:

            edges.append((i, j, graph[i][j]))

edges.sort(key=lambda x: x[2])

parent = [i for i in range(V)]


def find(x):

    while parent[x] != x:

        x = parent[x]

    return x


def union(u, v):

    parent_u = find(u)
    parent_v = find(v)

    parent[parent_v] = parent_u


mst = []
total_cost = 0

for u, v, wt in edges:

    if find(u) != find(v):

        mst.append((u, v, wt))

        total_cost += wt

        union(u, v)

print("MST Edges:", mst)

print("Total Cost:", total_cost)