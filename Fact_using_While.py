# Factorial using While loop
def factorial(n):
    num = n
    i = 1
    while i < num:
        r = n * i
        n = r
        i += 1
    return r


fact = int(factorial(5))
print(fact)
