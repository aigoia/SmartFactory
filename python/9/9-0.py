def factorial(n):
    print("n >>", n)
    
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(3))