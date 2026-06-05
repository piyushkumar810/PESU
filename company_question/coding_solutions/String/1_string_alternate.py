'''
Question: Merge Strings Alternately
You are given two strings word1 and word2.
Merge the strings by taking characters alternately from each string, starting with word1.
If one string is longer than the other, append the remaining characters of the longer string to the end of the merged string.
Return the merged string.

Example 1:

Input:
word1 = "abc"
word2 = "pqr"

Output:
"apbqcr"

Explanation:

word1 : a b c
word2 : p q r

merged: a p b q c r

Example 2:

Input:
word1 = "ab"
word2 = "pqrs"

Output:
"apbqrs"

'''

def alternate_string(word1,word2):
    result=""

    n=min(len(word1),len(word2))
    for i in range(n):
        result += word1[i]
        result += word2[i]
    
    result += word1[n:]
    result += word2[n:]

    return result


word1="abc"
word2="pqr"
print(alternate_string(word1,word2))