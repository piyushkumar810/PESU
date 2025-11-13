x = 10

def change():
    global x   # tells Python: “use the global x”
    x = 5
    print("Inside function:", x)

change()
print("Outside function:", x)
