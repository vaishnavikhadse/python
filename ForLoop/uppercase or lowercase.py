
x=input('enter any char')
y= ord(x)
print(y)
if y>=65 and y<=90:
    print("capital")
elif y>=97 and y<=122:
    print("small")
elif y>=48 and y<=57:
    print("Digit")
else:
    print("I dont know this char")

