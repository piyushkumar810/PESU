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
print()


print("q5. calculate the area and circumfrence of the circle given its radius")
def circle():
    radius=int(input("enter the radius of the circle"))
    pie=3.14
    print(f"area of circle = {pie*radius*radius}")
    print(f"circumfrence of the circle = {2*pie*radius}")
circle()
print()


print("q6. wap to check the type of input entered by the user")
def check_typeOf():
    a1=30
    a2=30.3
    a3="piyush"
    a4=["piyush kumar", 27, "MCA"]
    a5=(1,2,3,4,5)
    a6={"piyush kumar", 27, "MCA"}
    a7={"name":"piyush kumar",
        "roll":27,
        "course":"MCA"}
    
    print(f"type of a1 : {type(a1)}")
    print(f"type of a2 : {type(a2)}")
    print(f"type of a3 : {type(a3)}")
    print(f"type of a4 : {type(a4)}")
    print(f"type of a5 : {type(a5)}")
    print(f"type of a6 : {type(a6)}")
    print(f"type of a7 : {type(a7)}")

check_typeOf()
print()


print("q7. accept a number from the user and print square and cube")
def SquareOfNo():
    inpu=int(input("enter the  number : "))
    print(f"the square of the number is {inpu**2}")
    print(f"the cube of the number is {inpu**3}")

SquareOfNo()
print()


print("q8. wap to converrt second into hour, minuets and second formate")
def second_conversion():
    second=int(input("enter the second :"))
    hour=second/3600
    minute=second/60
    print(f"second is converted into this much hr{ hour} and min{ minute}")

second_conversion()
print()


print("q9. take the three digit number from the user and find the sum of its digit")
def sumOfDigit():
    digit=int(input("enter 3 digit number : "))
    sum=0
    quent=digit/10
    while(digit!=0):
        rem=digit%10
        

print("q10. accept marks in 5 subjects, calculate the sum and average")
def result():
    marks={"operating system " : 75,
           "dsa with c ": 80,
           "pyhton " : 78,
           "software development ": 85,
           "dbms ": 80}
    total_mark=marks["dbms"]+marks["dsa with c"]+marks["operating system"]+marks["pyhton"]+marks["software development"]
    average_marks=total_mark/5

    print(f"total marks obtained is {total_mark}")
    print(f"the average of the total marks {average_marks}")

result()