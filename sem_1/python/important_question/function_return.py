# function can return multiple values

def get_values():
    x = 10
    y = 20
    z = 30
    return x, y, z  # returning multiple values

# Calling the function
a, b, c = get_values()

print("a =", a)
print("b =", b)
print("c =", c)


# scope of the function
def outerFunc():
    sample_str = 'Outer Function'
    def innerFunc():
        sample_str = 'Inner Function'
        print(sample_str)
    innerFunc()
    print(sample_str)
outerFunc()
