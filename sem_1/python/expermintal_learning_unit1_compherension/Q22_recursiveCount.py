# Write a recursive function to count vowels in a string.

# Recursive function to count vowels in a string
def count_vowels(s):
    vowels = "aeiouAEIOU"
    
    # Base case: empty string
    if s == "":
        return 0
    
    # Check first character + recurse for remaining string
    if s[0] in vowels:
        return 1 + count_vowels(s[1:])
    else:
        return count_vowels(s[1:])

# Example usage
string = input("Enter a string: ")
print("Number of vowels:", count_vowels(string))
