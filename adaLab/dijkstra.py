class Solution:

    def dijkstra(self, V, graph, S):

        # Distance array
        dist = [float('inf')] * V
        dist[S] = 0

        # Visited array
        visited = [False] * V

        # Process all vertices
        for _ in range(V):

            # Find minimum distance unvisited node
            min_dist = float('inf')
            u = -1

            for i in range(V):

                if not visited[i] and dist[i] < min_dist:

                    min_dist = dist[i]
                    u = i

            # Mark node as visited
            visited[u] = True

            # Traverse all adjacent vertices
            for v in range(V):

                # Check:
                # 1. Edge exists
                # 2. Vertex not visited
                # 3. Relaxation possible
                if (graph[u][v] != 0 and
                    not visited[v] and
                    dist[u] + graph[u][v] < dist[v]):

                    dist[v] = dist[u] + graph[u][v]

        return dist


# Input
V = int(input())

graph = []

for _ in range(V):

    row = list(map(int, input().split()))

    graph.append(row)

S = int(input())

# Run Dijkstra
obj = Solution()

result = obj.dijkstra(V, graph, S)

print(result)