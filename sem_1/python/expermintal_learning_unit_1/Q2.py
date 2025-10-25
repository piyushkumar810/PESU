'''
Using a loop, collect 10 shopping items as input. Use a Counter to count 
occurrences and display the most common item. If there’s a tie, display all tied items.
'''
list_of_items=[]
for i in range(3):
    item=input(f"enter list_of_items {i+1}: ").strip().lower()
    list_of_items.append(item)
    
item_count={}
for item in list_of_items:
    if item in item_count:
        item_count[item] +=1
    else:
        item_count[item]=1
        
max_frequency=max(item_count.values())

most_common_item=[]
for item,count in item_count.items():
    if count==max_frequency:
        most_common_item.append(item)
        
print("\n most common item(s): ")
for item in most_common_item:
    print(f"{item}: {item_count[item]} times")
    