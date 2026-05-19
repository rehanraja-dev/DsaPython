arr = [11,2,3,2,4,2,4,3,7,7,7,7,7]
n = len(arr)
maxCount = 0
result = 0
for i in range(n):
    count = 0 

    for j in range(n):
        if arr[i] == arr[j]:
            count += 1

    if count > maxCount:
        maxCount = count
        result = arr[i]

print(f"{result} is the most frequent and its frequency is: {maxCount}")