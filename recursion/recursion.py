
# count = 0

# def star():
#     for i in range(1,6):
#         for j in range(1,i+1):
#             print("*", end=" ")
#         print()

# star()

# def recursive_triangle(rows):
#     if rows == 0:
#         return 
    
#     recursive_triangle(rows-1)
#     print("* " * rows)

# recursive_triangle(5)

# def recursive_diamond(rows):
#     if rows == 1:
#         print("*")
#         return
#     print("* "* rows)
#     recursive_diamond(rows-1)
#     print("* "* rows)

# recursive_diamond(5)



#sum of 1 to N using recursion


# def sum(n, s=0):
#     if n == 0:
#         print(s)
#         return
#     i = n
#     sum(n-1, s+i)

# sum(10)

# def addition(num):
#     if num == 0:
#         return 0
#     else:
#         return num + addition(num-1)

# print(addition(10))

def fac(num):
    if num == 1:
        return 1
    return num * fac(num - 1)

print(fac(3))

