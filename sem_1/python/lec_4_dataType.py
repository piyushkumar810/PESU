a=11
b=2.8
c=1+3j

# convert from int to float
x=float(a)
print(x)
print()

# convert from float to int
y=int(b)
print(y)
print()

# convert from int to complex
z=complex(a)
print(z)
print()

# NOTE:-  can i convert complex no to int --> we cannot convert it directly but yes if we convert complex to striing and then string to int
# the reasion behind it is :- 

# ----------------------------------- string---------------------------------------------
# string is a sequence of unicode character
print("\u03c0")
print("\u0906")
print()

# exapmples
s1="hello"
s2="world \n hi"
s3='''hi there 
i am piyush 
this side'''

print(s1)
print(s2)
print(s3)
print()

print(f"method of string :- find() ")
txt="python programming"
print(txt.find("pro"))  # 7
print(txt.find("xyz"))  #-1, it gives -1 means char not found
print()

print(f"method of string :- partition() ")
txt="python programming"
print(txt.partition("pro"))  # ('python ', 'pro', 'gramming') it return result in tuple
print()

print(f"method of string :- split() ")
txt="python programming"
print(txt.split())           #['python', 'programming']
print(txt.split("o"))        #['pyth', 'n pr', 'gramming']
print()

print(f"method of string :- find() ")
txt="python programming"
print(txt.find("pro"))  
print(txt.find("xyz")) 
print()