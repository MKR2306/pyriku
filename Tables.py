# Tables
n = int(input("Enter the number: "))
i = 1

while i<=10:
    print(n,"*",i,"=",(n*i))
    i+=1

print()
print()

for j in range(1,11):
    print(n,"*",j,"=",(n*j))