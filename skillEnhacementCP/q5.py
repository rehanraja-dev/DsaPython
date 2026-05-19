a = [1,2,3,4,5,6,7]
k = 2
n = len(a)

temp = []
for i in range(0,k):
    temp.append(a[i])
print(temp)
for i in range(0,n-k):
    a[i] = a[i+k]
   
for i in range(0, k):
    a[n - k + i] = temp[i]

print(a)