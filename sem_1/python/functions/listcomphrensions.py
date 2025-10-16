res=[]
for _ in range(5):
    res.append('hello')
print(res)

# we can do these all things in one line
print()
world=["hello" for _ in range(5)]
print(world)

print()
print("Q1. Find the square of the numbers using list comprehension")

numbers = [2, 4, 6, 8, 10]
squares = [x**2 for x in numbers]
print("The squares are:", squares)


# conditional list comprehension
numbers1=[1,2,3,4,5,6,7,8,9,10]
square_of_evens=[x**2 for x in numbers1 if x%2 ==0]
print(square_of_evens)

print("q2. take a list of 3 string value and the first letter or the string should be capatilized")
input1=['apple', 'mango', 'litchi']
# output shoule be = ['A' , 'M', 'L']
capt=[n[0].upper() for n in input1]
print(capt)

