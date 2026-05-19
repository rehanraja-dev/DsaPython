a = [1,2,3,43,3,4,64,12]

i = 1
# j = i+1
n = len(a)
# a.sort()
# while j < n :
#     if a[i] < a[j]:
#         a[i],a[j] = a[j],a[i]

#     else:
#         i += 2
#         j +=2

while i < n-1:
    if a[i-1] < a[i] < a[i+1]:
        a[i],a[i+1] = a[i+1],a[i]
        



print(a)