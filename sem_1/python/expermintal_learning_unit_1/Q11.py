'''
Create check_strength(password) that checks: 
≥8 characters
at least one uppercase, lowercase, digit, and special character
Return “Strong” or “Weak”.
'''

def check_string_strength(password):
    has_upper=False
    has_lower=False
    has_digit=False
    has_special=False
    
    if len(password)>=8:
        for ch in password:
            if ch.isupper():
                has_upper=True
            elif ch.islower():
                has_lower=True
            elif ch.isdigit():
                has_digit=True
            else:
                has_special=True
                
        if has_upper and has_lower and has_digit and has_special:
            return "strong"
        else:
            return "weak"
    else:
        return "weak"
        

passw="Hello@123"
result=check_string_strength(passw)
print("password strength: ", result)
        