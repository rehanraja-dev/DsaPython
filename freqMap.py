number = [1,2,3,4,12,3,4,5,1,2,34,5]

frequency = {}

# for n in number:
#     if frequency.get(n):
#         frequency[n] += 1
#     else:
#         frequency[n] = 1

# print(frequency.get(122))
# print(frequency[1])

for n in number:
     frequency[n] = frequency.get(n, 0) + 1

print(frequency)