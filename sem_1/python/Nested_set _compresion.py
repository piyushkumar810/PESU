# ------------------------------------- set comprehension---------------------------------

# 1st -> simple set
# {expr for variable in iterable}
sentence="the cat in a hat have two, siddekicks in a, "
words=sentence.lower().replace("."," ").replace(","," ").split()
unique_words={words for words in words}
print(unique_words)

# 2nd-> conditional set comprehension
print()
short={word for word in words if len(word)<=3}
print(short)


res={x*y for x in range(4) if x%2==0
     for y in range(5) if y>2}
print(res)
print(type(res))

print("Q1. square of number from 1 to 7")
sqrt={x*x for x in range(1,8)}
l3=list(sqrt)
l4=l3.sort()
print(sqrt)
print(l3)
print(l4)


# unique chara
name = "piyushi"
unique = ""

for ch in name:
    if ch not in unique:
        unique += ch

print(unique)


print("Q2. print unique character")
str="piyushi"
uni={ch for ch in str}
print(uni)


print("Q3. create a set of fruits that have more than")
fruits=["apple", "orange", "mango", "watermelon", "grapes"]
slkd={fruit for fruit in fruits if len(fruit)>5}
print(slkd)

print("Q4. create a set of all no that are both even and divisible by 3 betwee 1 -50")

# using normal for loop
for i in range(1,51):
    if(i%2==0 and i%3==0):
        print(i)

# using set
even_and_div={i for i in range(1,51) if(i%2==0 and i%3==0)}
print(even_and_div)

# prime no
# 5 is a prime no which is only divisible by 1 iand itself

i=0
for i in range(1,51):
    print(i)

