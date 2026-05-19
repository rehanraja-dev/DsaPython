number = int(input())
# print(type(number))
temp = number
# print(type(temp))
pallendromNum = 0
count = 0
while temp > 0:
    a = temp % 10
    pallendromNum = pallendromNum * 10 + a
    temp = temp//10
    count = count + 1
    # print("hello")
if pallendromNum == number:
    print(f"{number} is pallendrom number")
else:
    print(f"{number} is not pallendrom number")
