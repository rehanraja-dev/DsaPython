INF = float('inf')



def all_paired(graph):
  
    V = len(graph)
    
  
    L = [list(row) for row in graph]
   
    for k in range(V):       
        for i in range(V):   
            for j in range(V): 
                
               
                if L[i][k] + L[k][j] < L[i][j] and i != j:
                    L[i][j] = L[i][k] + L[k][j] 
    print_matrix(L)


def print_matrix(matrix):
    # print("Final Shortest Distances Between All Nodes")
    for row in matrix:
       
        print([x if x < 99990 else "INF" for x in row])


my_graph = [
    [0,   4,   11],  
    [6,   0,   2],  
    [3, INF, 0]
]

all_paired(my_graph)

