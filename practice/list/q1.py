# Python - Change List Item

# Using Index
list = [10,20,30,40]
list[0] = 20
print(list)

# Using Slicing for Multiple Items
list = [10,20,30,40]
list[1:3] = 30,40
print(list)

# Using List Comprehension
list = [10,20,30,40]
list = [x*2 if x%2==0 else x for x in list]     # Doubling even numbers
print(list)


# Using a Loop with enumerate()
list = [10,20,30,40]
for i,v in enumerate(list):
    if v % 2 == 0:
        list[i] +=5                             #Adding 5 to odd numbers
print(list)

