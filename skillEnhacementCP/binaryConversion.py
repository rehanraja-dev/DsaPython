def decimal_to_binary(n):
    if n == 0:
        return "0"
    binary_digits = []
    while n > 0:
        remainder = n % 2       
        binary_digits.append(remainder)
        n = n // 2            
    return binary_digits

binary = decimal_to_binary(2000)
count = 0
n = len(binary)
print(binary)

for i in range(n):
    if binary[i] == 1:
        count += 1

print(count)