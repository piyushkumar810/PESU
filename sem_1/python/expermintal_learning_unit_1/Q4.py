'''
Read N integers; build OrderedDict to keep first occurrence only. Print unique sequence preserving input order.
'''
from collections import OrderedDict

user_input=int(input("Enter how many numbers: "))

numbers=[]

for i in range(user_input):
    num=int(input(f"enter number {i+1}: "))
    numbers.append(num)
    
unique_num=OrderedDict()
for num in numbers:
    if num not in unique_num:
        unique_num[num]=True
        
print("Unique sequence: ")
for num in unique_num.keys():
    print(num, end=' ')