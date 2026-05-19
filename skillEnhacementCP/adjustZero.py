arr = [0,2,4,0,5,0,1,3]

# p = len(arr)-1

# for i in range(0,len(arr)-1):
#     if arr[i] == 0 and arr[p] != 0:
#         arr[p],arr[i] = arr[i],arr[p]
#         p = p-1

i = 0
j = 0

while i < len(arr)-1 and j < len(arr)-1:
    if arr[i] == 0:
        i += 1
    if arr[j] != 0:
        j += 1
    
    if arr[i] != 0 and arr[j] == 0:
        arr[j],arr[i] = arr[i],arr[j]


print(arr)

