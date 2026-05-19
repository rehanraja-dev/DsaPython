a = []
b = []
 
for x in input().split():
    a.append(int(x))

for x in input().split():
    b.append(int(x))

i = 0
j = 0
result = []
while i < len(a) and j < len(b):
    if a[i] == b[j]:
        result.append(a[i])
        i = i + 1
        j = j + 1
    else:
        j = j + 1
print('[]') if len(result) == 0 else print(*result)
