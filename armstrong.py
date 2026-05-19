number = int(input())
temp = number
size = len(str(number))
armstrongNumber = 0

while temp > 0:
    lastDigit = temp % 10
    armstrongNumber = armstrongNumber + lastDigit ** 3
    temp = temp // 10 

if armstrongNumber == number:
    print(f"{number} is armstrong number")
else:
    print(f"{number} is not armstrong number")