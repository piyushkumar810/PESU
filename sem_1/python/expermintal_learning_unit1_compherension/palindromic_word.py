# Extract all palindromic words from a given list of words using list comprehensions

list1=["131","rahils","raejsih","madam","raghav","1221","labal","kaufdf","racecar"]

palindromic_word=[word for word in list1 if(word==word[::-1])]
print(palindromic_word)