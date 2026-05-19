# rows, cols = map(int, input("Enter rows and columns: ").split())
# matrix = []
# for i in range(rows):
#     row = list(map(int, input(f"Enter row {i+1}: ").split()))
#     matrix.append(row)
# print(matrix)


V = 5

adj = [[] for _ in range(V)]

adj[0].append((1, 2))
adj[0].append((2, 4))

adj[1].append((2, 1))
adj[1].append((3, 7))

adj[2].append((4, 3))

adj[3].append((4, 2))

print(adj)
