def binary_conversion(n):
    if n == 0:
        return "0"
    binary_digits = []

    while n:
        remainder = n % 2
        binary_digits.append(remainder)
        n = n // 2
    return binary_digits

num = int(input())
binary = binary_conversion(num)
n = len(binary)
count = 0

for i in range(n):
    if binary[i] == 1:
        count += 1

if count == 1:
    print(True)

else:
    print(False)


# def is_power_of_two(n):
 
#     return n > 1 and (n & (n - 1)) == 0 


# print(is_power_of_two(16)) 
# print(is_power_of_two(1))  
# print(is_power_of_two(0))   
# print(is_power_of_two(18))  





decimal = int(input())

while n:
    remiander = decimal % 2
    
