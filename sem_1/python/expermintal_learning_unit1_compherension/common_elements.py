# Given two lists, find all elements that are common using set comprehension.

list1=[1,2,3,4,5,6,7,8,9,10]
list2=[1,4,6,8,10,11,51]

# using set comprenhension
common_element_list={common_element for common_element in list1 if common_element in list2}

print(common_element_list)