a = [2,3,5,7,9,12,14]


def merge(a ,low ,mid ,high):
    i = low
    j = mid + 1
    c = []
    while i <= mid and j <= high:
        if a[i] < a[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(a[j])
            j += 1

    while i <= mid:
        c.append(a[i])
        i += 1

    while j <= high:
        c.append(a[j])
        j += 1
    

def mergeSort(a ,low ,high):
    if low < high:
        mid = (low - (high - low)) // 2
        mergeSort(a ,low ,mid)
        mergeSort(a ,mid+1 ,high)
        merge(a ,low ,mid ,high)

mergeSort(a, 0, len(a)-1)

print(a)    

