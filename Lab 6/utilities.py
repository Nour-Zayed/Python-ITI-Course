import random
import string
import re

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

def format_phone_number(phone):
    digits = re.sub(r'\D', '', phone) 
    if len(digits) == 11 and digits.startswith('0'):
        formatted = f'+20 {digits[1:4]} {digits[4:7]} {digits[7:]}'
        return formatted
    else:
        return "Invalid phone number"
