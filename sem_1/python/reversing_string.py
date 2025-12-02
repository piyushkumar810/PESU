def reverse_string(inp):
    result = []
    for i in range(len(inp)-1, -1, -1):   # start → end → step
        result.append(inp[i])
    return "".join(result)

n = input("Enter the string value: ")
print("Reversed string:", reverse_string(n))


# -------------------------- string palindrom
def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            print("No, it is not a palindrome")
            return
        left += 1
        right -= 1

    print("Yes, it is a palindrome")

n = input("Enter a string: ")
is_palindrome(n)