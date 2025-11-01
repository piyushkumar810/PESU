# Given a list of temperatures in Celsius, convert them to Fahrenheit using list comprehension.

list1=[10,40,50,100,-10]
convert_in_fahrenheit=[(fahrenheit*9/2)+32 for fahrenheit in list1]
print(convert_in_fahrenheit)
