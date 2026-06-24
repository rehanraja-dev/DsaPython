def get_prime_factors(num):
    factors = []
    
    
    while num % 2 == 0:
        factors.append(2)
        num //= 2
        
    
    i = 3
    while i * i <= num:
        while num % i == 0:
            factors.append(i)
            num //= i
        i += 2
        
    
    if num > 1:
        factors.append(num)
        
    return factors

num = int(input())
print(get_prime_factors(num))  
