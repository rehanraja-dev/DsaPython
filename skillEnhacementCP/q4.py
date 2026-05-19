a = [1,2,3,4,5,6,7]
k = 2
n = len(a) - 1 
i = k
counter = 0
while(True):
    print(a[i], end = '  ')
    i += 1
    if i % n == 0:
        i = 0
    counter += 1
    if counter == n:
        break
    
    
    

