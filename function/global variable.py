x=20
def show():
    #local
    x=20
    print(x)
    #global
show()
print(x)
print("#################################################")

x=10
def show():
    global x
    x=20
    print(x)
show()
print(x)