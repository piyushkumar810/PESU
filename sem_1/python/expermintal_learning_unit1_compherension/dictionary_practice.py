# Given a list of numbers, create a dictionary with number as key and cube as value only if number is even

list1=[1,4,7,6,8,3,12,34,5,2]

dict_cube_of_even={key:(key**3) for key in list1 if(key % 2==0)}

print(dict_cube_of_even)