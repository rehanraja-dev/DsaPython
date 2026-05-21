class Solution:

    def prims(self, V, graph):

        weight = [float('inf')] * V
        visited = [False] * V
        parent = [-1] * V
        weight[0] = 0

        for _ in range(V):

            min_weight = float('inf')
            u = -1

            for i in range(V):

                if not visited[i] and weight[i] < min_weight:

                    min_weight = weight[i]
                    u = i

            visited[u] = True

            for v in range(V):

              
                if (graph[u][v] != 0 and
                    not visited[v] and
                    graph[u][v] < weight[v]):

                    weight[v] = graph[u][v]

                    parent[v] = u

        total_cost = 0

        print("Edges in MST:")

        for i in range(1, V):

            print(parent[i], "-", i, "weight =", graph[parent[i]][i])

            total_cost += graph[parent[i]][i]

        print("Total Cost =", total_cost)



graph = [
    [0, 2, 4, 0],
    [2, 0, 1, 7],
    [4, 1, 0, 3],
    [0, 7, 3, 0]
]

V = len(graph)
obj = Solution()
obj.prims(V, graph)