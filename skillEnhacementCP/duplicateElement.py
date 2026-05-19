a = [2,2,2,3,3,4]

if a:
    j = 0
    for i in range(1, len(a)):
        if a[i] != a[j]:
            j += 1
            a[j] = a[i]

    a = a[0:j + 1]

print(a)