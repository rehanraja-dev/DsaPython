def heapify(arr, n, i):
    largest = i
    left = 2 * i 
    right = 2 * i + 1

    # Check if left child exists and is greater than root
    if left < n and arr[i] < arr[left]:
        largest = left

    # Check if right child exists and is greater than current largest
    if right < n and arr[largest] < arr[right]:
        largest = right

    # If root is not largest, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # 1. Build a Max-Heap from the input array
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # 2. Extract elements one by one
    for i in range(n - 1, 0, -1):
        # Move current root (largest) to the end
        arr[i], arr[0] = arr[0], arr[i]
        # Restore heap property on the reduced heap
        heapify(arr, i, 0)
    
    return arr

# Example Usage
data = [12, 11, 13, 5, 6, 7]
print(f"Sorted Array: {heap_sort(data)}")
