# Write a user-defined function that takes a string and returns its length.(Do not use len)

# User-defined function to find length of a string
def string_length(s):
    count = 0
    for char in s:
        count += 1
    return count

# Example usage
string = input("Enter a string: ")
print("Length of the string is:", string_length(string))
