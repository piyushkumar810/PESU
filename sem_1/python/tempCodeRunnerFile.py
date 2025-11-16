def outer():
    x21 = 10
    def inner():
        x21 = 20
    inner()
    print(x21)

outer()

