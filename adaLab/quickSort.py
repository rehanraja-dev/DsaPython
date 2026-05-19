def partition(array ,low ,high):
    pivot =  low
    i = low + 1
    j = high
    while True:
        while i<=j and array[i] <= array[pivot]:
            i = i + 1
        while i<=j and array[j] > array[pivot]:
            j = j - 1
        if i <= j:
            array[i],array[j] = array[j],array[i]
        else:
            break

        array[low],array[j] = array[j],array[low]
        return j


def quickSort(array,low ,high):
    if low < high:
        p = partition(array ,low, high)
        quickSort(array ,low ,p-1)
        quickSort(array ,p+1 ,high)
    return array


array = [7,2,9,3,11,4,8,16,5,13]
low = 0
high = len(array)-1

print(quickSort(array,low ,high))