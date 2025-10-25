'''
Read N words; use defaultdict(list) to group anagrams. Print only groups with size ≥ 3.
'''

from collections import defaultdict

input_no_of_words=int(input("enter number of words: "))

words=[]
for i in range(input_no_of_words):
    word=input(f"enter words {i+1}: ").strip().lower()
    words.append(word)
    
groups=defaultdict(list)
for word in words:
    key=''.join(sorted(word))
    groups[key].append(word)
    
print("\ngroups with size >= 3:")
for group in groups.values():
    if len(group)>=3:
        print(group)