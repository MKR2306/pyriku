# Binary Converter
def binary(number):
    i = 0
    r = []
    bin = ""
    while number > 0:
        r.append(number % 2)
        number = int(number / 2)
        bin = bin + str(r[i])
        i += 1
    reverse(bin)


def reverse(number):
    i = len(number)-1
    bin = ""
    while i >= 0:
        bin = bin + (number[i])
        i = i - 1
    print(bin)


n = int(input("Enter a decimal number: "))
print("Binary of",n,":")
binary(n)