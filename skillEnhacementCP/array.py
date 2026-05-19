# array1 = []
# array2 = []
# array3 = []
# arrayCommon = []

# print("Enter the size of array1: ")
# m = int(input())
# print("Enter the size of array2: ")
# n = int(input())
# print("Enter the size of array3: ")
# o = int(input())

# print(f"Enter the {m} elements for array1: ")
# for i in range(0, m):
#     array1.append(int(input()))

# print(f"Enter the {n} elements for array2: ")
# for i in range(0, n):
#     array2.append(int(input()))

# print(f"Enter the {o} elements for array3: ")
# for i in range(0, o):
#     array3.append(int(input()))

# for i in range(0, m):
#     for j in range(0, n):
#         for k in range(0, o):
#             if array1[i] == array2[j] and array2[j] == array3[k]:
#                 if array1[i] not in arrayCommon:
#                     arrayCommon.append(array1[i])

# print("Common elements are:", arrayCommon)





# array1 = []
# array2 = []
# array3 = []
# arrayCommon = []

# print("Enter the size of array1: ")
# m = int(input())
# print("Enter the size of array2: ")
# n = int(input())
# print("Enter the size of array3: ")
# o = int(input())

# print(f"Enter the {m} elements for array1: ")
# for i in range(0, m):
#     array1.append(int(input()))

# print(f"Enter the {n} elements for array2: ")
# for i in range(0, n):
#     array2.append(int(input()))

# print(f"Enter the {o} elements for array3: ")
# for i in range(0, o):
#     array3.append(int(input()))

# for i in range(0, m):
#     for j in range(0, n):
#         if array1[i] == array1[j]:
#             for k in range(0, o):
#                 if array2[j] == array3[k]:
#                     if array1[i] not in arrayCommon:
#                         arrayCommon.append(array1[i])
#                     break
#             break

# print("Common elements are:", arrayCommon)


array1 = []
array2 = []
array3 = []
arrayCommon = []

print("Enter the size of array1: ")
m = int(input())
print("Enter the size of array2: ")
n = int(input())
print("Enter the size of array3: ")
o = int(input())

print(f"Enter the {m} elements for array1: ")
for i in range(0, m):
    array1.append(int(input()))

print(f"Enter the {n} elements for array2: ")
for i in range(0, n):
    array2.append(int(input()))

print(f"Enter the {o} elements for array3: ")
for i in range(0, o):
    array3.append(int(input()))

i = 0
j = 0
k = 0

while i <= j and j <= k:
    if array1[i] == array2[j] and array2[j] == array3[k]:
        if array1[i] not in arrayCommon:
            arrayCommon.append(array1[i])
            i = i + 1
            j = j + 1
            k = k + 1
    if array1[i] < array2[j] and array1[i] < array3[k]:
        i = i + 1
    elif array2[j] < array3[k]:
        j == j + 1
    else:
        k == k + 1

print("Common elements are:", arrayCommon)