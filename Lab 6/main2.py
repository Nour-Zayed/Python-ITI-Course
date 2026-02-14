
from utilities import generate_password, validate_email, format_phone_number

print("Password:", generate_password(12))

email = "Nour@m.com"
print(f"Is '{email}' a valid email?", validate_email(email))

phone = "01050005703"
print("Formatted Phone:", format_phone_number(phone))
