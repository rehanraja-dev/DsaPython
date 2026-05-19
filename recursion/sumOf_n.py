def sum(num):
    if num == 1:
        return 1
    return num + sum(num - 1)

num = int(input())
print(f"Sum of 1 to {num} is {sum(num)}")