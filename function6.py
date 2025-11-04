def ispal(n):
    n=str(n)
    return n==n[::-1]
print(ispal(345))
print(ispal(2332))