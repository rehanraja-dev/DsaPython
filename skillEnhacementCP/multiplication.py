def multiply_except_self(nums):
    n = len(nums)
    preP = [1] * n
    sufP = [1] * n

    # Step 1: Calculate prefix products (left side)
    prefix = 1
    for i in range(n):
        preP[i] = prefix
        prefix = prefix * nums[i]

    # Step 2: Calculate suffix products (right side) and multiply
    suffix = 1
    for i in range(n - 1, -1, -1):
        sufP[i] *= suffix
        suffix = suffix * nums[i]

    return [preP[i] * sufP[i] for i in range(n)]

# Example usage:
arr = [1, 2, 3, 4]
print(multiply_except_self(arr)) 
