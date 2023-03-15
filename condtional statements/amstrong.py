a=int(input('Enter a Number'))
b=a//100
c=a%100
d=c//10
e=c%10
f=b**3+d**3+e**3
if a==f:
    print("Armstrong number")
else:
    print("Not armstrong number")