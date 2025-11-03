for num in range(-2,-5,-1):
   print(num, end=", ")


x = 0
for i in range(10):
   for j in range(-1, -10, -1):
       x += 1 
print(x)

x1 = 0
# PROGRAMMING WITH PYTHON
# Review of Conditions and Loops
while (x1 < 100):
    x1+=2
print(x1)


numbers = [10, 20]
items = ["Chair", "Table"]
for x in numbers:
    for y in items:
       print(x, y)


x = 0; a = 5; b = 5
if a > 0:
    if b < 0: 
        X = x + 5
    elif a > 5: 
        x = x + 4
    else: 
        x = x+3
else: 
    x = x+ 2
print(x)
