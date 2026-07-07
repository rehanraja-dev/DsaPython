# Replace Values in a List in Python

# Using List Indexing
list = [10,20,30,40]
list[2] = 99
print(list)

# Using List Comprehension
list = [10,20,30,40]
list = [99 if x == 30 else x for x in list]
print(list)



