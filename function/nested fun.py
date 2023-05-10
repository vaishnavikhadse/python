def outer():
    print("In outer")
    msg="hello world"
    print(msg)
def inner():
    msg1="hello"
    print("In inner")
    print(msg1)


inner()
outer()