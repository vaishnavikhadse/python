from math import  pi
pi=3.14
def outer():
    pi=3.142
def inner():
    pi=3.12345
print(pi)

inner()
outer()