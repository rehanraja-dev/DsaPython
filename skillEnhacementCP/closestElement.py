a = [10,15,28,39,40]
b = [4,7,10,20,29]
x = 43
pair = []
diff = float('inf')
n = len(a)
m = len(b)

for i in range(0,n-1):
    for j in range(0,m-1):
        curr = abs((a[i]+b[j])-x)
        if curr < diff:
            diff = curr
            pair[0] = a[i]
            pair[1] = b[j] 

# l = a[0]
# r = b[-1]

# while l < n and r >= 0:
#     curr = abs((a[l]+b[r])-x)
#     if curr < diff:
#         diff = curr
#         pair[0] = a[l]
#         pair[1] = b[r]

#     if ((a[l] + b[r])) < x:
#         l += 1
#     else:
#         r -= 1

print(pair)