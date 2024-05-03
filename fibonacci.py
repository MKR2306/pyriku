# fibonacci series using for loop
n = 0
m = 1
result = 0
print( 0)
for i in range(10):
    result = n + m
    print(result)
    n = m
    m = result

# fibonacci series using while loop
j = 0
n1 = 0
n2 = 1
print()
print()
print(0)
result1 = 0
while j<10:
    result1 = n1+n2
    print(result1)
    n1 = n2
    n2 = result1
    j += 1
