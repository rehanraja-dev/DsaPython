num = int(input())
i = 2
# for i in range(2,num//2):
#     if num % i == 0:
#         print(f"{num} is not a prime number")
#         break
    
# if i == (num//2) - 1:
#     print(f"{num} is a prime number")

# count = 0
# for i in range(2,i*i<=num):
#     if num % i == 0:
#         print(f"{num} is not a prime number")
#         count += 1
#         break
    
# if count == 0:
#     print(f"{num} is a prime number")


def isPrime(num):
   
    if num <= 1:
        return False
    if num <= 3:
        return True
        

    if num % 2 == 0 or num % 3 == 0:
        return False
        

    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False  
        i += 6  
        
    return True


print(isPrime(num))  

