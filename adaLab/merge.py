# merge two array in sorted order

a = [2,5,7,9]
b = [3,6,8,10]
c=[]
i = 0
j = 0
n = len(a)
m = len(b)

while i < n and j < m:
    if a[i] == b[j]:
        c.append(a[i])
        i += 1
        j += 1 
    
    elif a[i] < b[j]:
        c.append(a[i])
        i += 1

    else:
        c.append(b[j])
        j += 1
        
print(c)