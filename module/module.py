######creating simple module###############
import mymodule
a=mymodule.add(100,200)
b=mymodule.sub(50,30)
print(a)
print(b)

print("######rename imported module############")
import mymodule as mm
a=mm.add(300,200)
b=mm.sub(100,50)
print(a)
print(b)

print("########importing only function from the module")
from mymodule import add,sub
a=add(100,200)
print(a)
b=sub(70,20)
print(b)

print("########importing everything from the module")
from math import*
from mymodule import*
a=add(100,300)
print(a)
b=sub(90,40)
print(b)
c=pow(10,2)
print(c)

print("###########hoe python find the module ")
from math import*
from mymodule import*
import sys
arr=sys.path
for p in arr:
    print(p)
