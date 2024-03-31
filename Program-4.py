import re

# Function to validate email addresses
def validate_email(email):
    # Define the email pattern
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9]+\.[a-z]{2,3}$'
    
    # Check if the email matches the pattern
    if re.match(pattern, email):
        return "Valid email"
    else:
        return "Invalid email"

# Test emails
emails = [
    "user@example.com",
    "user123@example.in",
    "user+test@example,com",
    "invalid-email",
    "user@example"
]

# Iterate through the emails and validate each one
for email in emails:
    print(f"{email}: {validate_email(email)}")
print('\n')


# Function to validate Bangladeshi mobile numbers
def validate_bangladesh_mobile_number(number):
    # Define the mobile number pattern
    pattern = r'^\+880[0-9]{10}$'
    
    # Check if the number matches the pattern
    if re.match(pattern, number):
        return "Valid Bangladeshi mobile number"
    else:
        return "Invalid Bangladeshi mobile number"

# Test mobile numbers
numbers = [
    "+880171234567",
    "8801987654321",
    "+801555555555",
    "+8801123456789", 
]

# Iterate through the numbers and validate each one
for number in numbers:
    print(f"{number}: {validate_bangladesh_mobile_number(number)}")
print('\n')

# Function to validate USA mobile numbers
def validate_USA_mobile_number(number):

    # Define the mobile number pattern
    pattern = r'^\+1[0-9]{3}[0-9]{7}$'
    
    # Check if the number matches the pattern
    if re.match(pattern, number):
        return "Valid USA mobile number"
    else:
        return "Invalid USA mobile number"

# Test mobile numbers
numbers = [
    "+11231234567",
    "+2347894561",
    "+17893216549",
]


# Iterate through the numbers and validate each one
for number in numbers:
    print(f"{number}: {validate_USA_mobile_number(number)}")
print('\n')

# Function to validate 16-character alphanumeric passwords
def validate_16digit_alphanum_pw(pw):
    
    # Define the mobile number pattern
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%])[A-Za-z0-9!@#$%]{16}$'
    
    # Check if the number matches the pattern
    if re.match(pattern, pw):
        return "Valid Password"
    else:
        return "Invalid Password"

# Test Passwords
passwords = [
    "1234ABCD1234abcd",
    "@123ABCD12ac3421",
    "1234ABCDabcd!@#$",
    "!12@ab#AB$34%cde"
]

# Iterate through the numbers and validate each one
for pw in passwords:
    print(f"{pw}: {validate_16digit_alphanum_pw(pw)}")