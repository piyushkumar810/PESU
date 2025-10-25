'''
Given a seed value of 5. Generate a password that is of 10 characters. 
At least one uppercase, lowercase, digit, and special character.
'''

import random
import string

def generate_password(seed_value):
    random.seed(seed_value)
    
    upper=string.ascii_uppercase
    lower=string.ascii_lowercase
    digits=string.digits
    special="!@#$%^&*()"
    
    password_list=[
        random.choice(upper),
        random.choice(lower),
        random.choice(digits),
        random.choice(special)
        ]
        
        
        
    all_character=upper+lower+digits+special
    for _ in range(6):
        password_list.append(random.choice(all_character))
    
    
    random.shuffle(password_list)
    
    password="".join(password_list)
    return password
    
    
passw=generate_password(5)
print("generated password: ", passw)
       