
arr = [2,4,6,8,10,7,5,3]
n = len(arr) - 1

# ----Brute Force to find peak----

# for i in arr:
#     if arr[i] < arr[i+1]:
#         continue
#     else:
#         peak = arr[i]
#         break

# print(peak)

# ----Optimal Solution----

peak = 0
i = 0
while i < n:
    mid = (i+n) // 2
    if arr[mid-1] < arr[mid] and arr[mid] > arr[mid+1]:
        peak = arr[mid]
        break
    
    else:
        if arr[mid-1] < arr[mid] and arr[mid+1] > arr[mid]:
            i = mid 
        else:
            n = mid

print(peak)



