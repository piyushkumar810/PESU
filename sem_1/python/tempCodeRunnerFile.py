x1=10
def change():
    #print(x1)  
    global x1
    x1=50
    print("inside the function: ", x1)

change()
print("outside the function but changing the global: ", x1)
print()