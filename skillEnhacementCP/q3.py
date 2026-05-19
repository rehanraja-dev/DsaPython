

# j = 0

# for i in range(0,len(a)-1):
#     for j in range(i+1,len(a)-1):
#         if a[i] <= a[j]:
#             print(a[j], end =' ')
    

a = [16,17,4,3,5,2]
n = len(a) - 1


i = 0
j = i + 1
while i <= n:
    if a[i] < a[j]:
        print(a[j], end='  ')
        i += 1
        j += 1
    else:
        j += 1
    if j == n:
        i += 1
        j = j + 1
        if i == n:
            j = j-1
if i == n:
    print(a[i])           

        
