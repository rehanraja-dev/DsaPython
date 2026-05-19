def find_unique_element(arr):
    result = 0
    for num in arr:
        result ^= num  
    return result

mixed_array = [2, 3, 5, 4, 5, 2, 3]

print(f"The unique element is: {find_unique_element(mixed_array)}")

