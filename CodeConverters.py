import Binary,HexaDeci
say = "yes"
while say != "no":
    print()
    print("Converters:\n1: Decimal To Binary\n2: Decimal To Hexadecimal")
    try:
        op = int(input("Enter Option[1 or 2]: "))
        num = int(input("Enter the decimal number: "))
    except ValueError as ve:
        print(ve)
    if op == 1:
        print("Binary of",num,"=")
        Binary.binary(num)
    elif op == 2:
        print("HexaDecimal value of",num,"=")
        HexaDeci.hexa(num)
    else:
        print("Invalid option!")
    say = input("Do you want to Continue?[yes/no]: ")