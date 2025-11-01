# Convert two lists — one of keys and one of values — into a dictionary./

list1=[1,2,3,4,5,6]
list2=["piyush","rohit","praneeth","priyanshu","prabhat","tanmay"]

dictionary_form={key:value for key, value in zip(list1,list2)}
print(dictionary_form)