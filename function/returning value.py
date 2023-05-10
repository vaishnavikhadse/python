def add(x,y):
    z=x+y
    return z
a=add(20,30)
print("addition is",a)
######################################
def area(r):
    a=3.14*r*r
    return a
p=area(1.2)
print("area is",p)
######################################
def calculate(x,y):
    p=x+y
    q=x-y
    return p,q
a,b=calculate(60,20)
print(a)
print(b)