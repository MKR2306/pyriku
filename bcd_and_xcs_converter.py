# BCD Converter and Excess 3 code of a decimal number
def bcd_converter(number):
    bcd = ""
    for n in number:
        if n == "0":
            bcd = bcd + "0000"
        elif n == "1":
            bcd = bcd + "0001"
        elif n == "2":
            bcd = bcd + "0010"
        elif n == "3":
            bcd = bcd + "0011"
        elif n == "4":
            bcd = bcd + "0100"
        elif n == "5":
            bcd = bcd + "0101"
        elif n == "6":
            bcd = bcd + "0110"
        elif n == "7":
            bcd = bcd + "0111"
        elif n == "8":
            bcd = bcd + "1000"
        elif n == "9":
            bcd = bcd + "1001"

    return bcd


def excess_three(number):
    xcs = ""
    for n in number:
        if n == "0":
            xcs = xcs + bcd_converter("3")
        elif n == "1":
            xcs = xcs + bcd_converter("4")
        elif n == "2":
            xcs = xcs + bcd_converter("5")
        elif n == "3":
            xcs = xcs + bcd_converter("6")
        elif n == "4":
            xcs = xcs + bcd_converter("7")
        elif n == "5":
            xcs = xcs + bcd_converter("8")
        elif n == "6":
            xcs = xcs + bcd_converter("9")
        elif n == "7":
            xcs = xcs + "1010"
        elif n == "8":
            xcs = xcs + "1011"
        elif n == "9":
            xcs = xcs + "1100"

    return xcs


n = str(input("Enter the decimal number: "))
bcd = bcd_converter(n)
xcs = excess_three(n)
print("Bcd value of", n, "is", bcd)
print("Excess 3 code of",n,"is",xcs)
