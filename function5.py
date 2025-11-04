def isprime(n):
    if n<2:
        return False
    else:
        for i in range(2,n+1):
            if n%i==0:
                return False
        return True
print(isprime(5))
print(isprime(15))
print(isprime(50))