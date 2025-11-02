# Use zip() and max() to find the student with the highest score from two parallel lists.

list1=["piyush","praneeth","rohit","priyanshu","tanmay"]
list2=[60,70,50,80,95]

max_mark_student=list(max(zip(list1,list2)))

print(max_mark_student)