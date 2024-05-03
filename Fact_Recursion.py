# Factorial using Recursion
def factorial(n):
    if n <= 1:
        return 1
    else:
        n_minus_one = (factorial(n - 1))
        fact = n * n_minus_one
        return fact


query = 'yes'
while query != 'no':
    n = int(input("Enter n: "))
    fac = int(factorial(n))
    print("Factorial of",n,"=",fac)
    query = input("do you want to continue?[yes/no]: ")
