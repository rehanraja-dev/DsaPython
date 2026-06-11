#Bitwise
N, L, R = list(map(int,input().split()))
A = (1 << (L-1)) - 1
B = (1 << R) - 1

mask = A ^ B

print(N | mask)