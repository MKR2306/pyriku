# Factorial using for loop
def factorial(n):
    for i in range(1,5):
        f = n * i
        n = f
    return f


fact = int(factorial(5))
print(fact)