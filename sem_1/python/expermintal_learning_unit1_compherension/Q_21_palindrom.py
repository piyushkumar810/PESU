# Write a recursive function to check whether a string is a palindrome.

# Recursive function to check if a string is palindrome
def is_palindrome(s):
    # Base case: if length is 0 or 1, it's a palindrome
    if len(s) <= 1:
        return True
    # Compare first and last characters, then recurse for the substring
    elif s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False

# Example usage
string = input("Enter a string: ")
if is_palindrome(string.lower()):
    print("Yes, it is a palindrome.")
else:
    print("No, it is not a palindrome.")
    