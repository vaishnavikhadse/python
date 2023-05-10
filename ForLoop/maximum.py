#take three numbers and print maximum number
a=int(input('enter number 1'))
b=int(input('enter number 2'))
c=int(input('enter number 3'))
if a>b and a>c:
    print("A is max")
elif b>a and b>c:
    print("B is max")
else:
    print("C is max")
