print("q1. write a python program to print your name, prn, and course")
def persional_details():
    name="piyush kumar"
    prn="PESU12020234367"
    course="MCA"
    print(f"my name is {name} , roll is {prn} and my course in which i enrolled is {course}")
persional_details()
print()


print("q2. take two number as input and print sum, difference, product and quotient")
def user_input():
    a=int(input("enter the first number : "))
    b=int(input("enter the second number : "))
    sum=a+b
    difference=a-b
    product=a*b
    quotient=a/b

    print(f"the sum of the number is {sum}")
    print(f"the difference of the number is {difference}")
    print(f"the product of the number is {product}")
    print(f"the quotient of the number is {quotient}")
user_input()
print()


print("q3. write a python program to swap two variable without using third variable")
def swap():
    a=20
    b=10
    print(f"befor swapping the value of a = {a}, b= {b}")
    temp=a
    a=b
    b=temp
    print(f"after swapping the value of a = {a}, b= {b}")
swap()
print()


print("q4. convert temperature form celcies to fahrenheit and fahrenheit to celcies")
print()

print("q5. calculate the area and circumfrence of the circle given its radius")
def circle():
    radius=int(input("enter the radius of the circle"))
    pie=3.14
    print(f"area of circle = {pie*radius*radius}")
    print(f"circumfrence of the circle = {2*pie*radius}")
circle()


print("q6. wap to check the type of input entered by the user")

print("q7. accept a number from the user and print square and cube")
print("q8. wap to converrt second into hour, minuets and second formate")
print("q9. take the three digit number from the user and find the sum of its digit")
print("q10. accept marks in 5 subjects, calculate the sum and average")