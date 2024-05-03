# comparing 3 numbers
def max(a,b,c):
    if a>b:
        if a>c:
            print(a,"is the largest!")
        else:
            print(c,"is the largest!")
    else:
        if b>c:
         print(b,"is the largest!")
        else:
            print(c,"is the Largest")

max(91,911,91)