def outer():
    print("In outer")
    msg="Hello world"
def inner():
    nonlocal msg
    msg="vaishnavi"
    print("In inner")
    print(msg)

inner()

outer()
