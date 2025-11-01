# Given a list of numbers, create a set of numbers divisible by both 2 and 3.

list1=[1,2,3,4,5,6,7,8,9,10]

divisible_by_2_and_3={num for num in list1 if(num%2==0 and num%3==0)}

print(divisible_by_2_and_3)