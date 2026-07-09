def dfs(vertex, graph, visited, traversal):
    visited[vertex] = True
    traversal.append(vertex)

    for neighbour in graph[vertex]:
        if not visited[neighbour]:
            dfs(neighbour, graph, visited, traversal)


vertices = int(input("Enter number of vertices: "))
edges = int(input("Enter number of edges: "))

graph = [[] for _ in range(vertices)]

print("Enter edges as: source destination")
for _ in range(edges):
    source, destination = map(int, input().split())
    graph[source].append(destination)
    graph[destination].append(source)

start = int(input("Enter starting vertex: "))

visited = [False] * vertices
traversal = []

dfs(start, graph, visited, traversal)

for vertex in range(vertices):
    if not visited[vertex]:
        dfs(vertex, graph, visited, traversal)

print("DFS traversal:", traversal)
