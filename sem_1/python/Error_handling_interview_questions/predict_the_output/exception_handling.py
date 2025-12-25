# Q1)

try:
    x = int("abc")
except ValueError:
    print("Invalid")
else:
    print("Valid")
finally:
    print("Done")
'''
output
invalid
done
'''

# Q2)
try:
    print(5 / 1)
except:
    print("Error")
else:
    print("Success")
'''output
5.0
success
'''