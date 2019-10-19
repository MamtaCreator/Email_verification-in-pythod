 #package to be needed :pip install validate_email,pip install py3DNS
#editor: jupiter notebook

from validate_email import validate_email
email = input('Input your email to verify: ')
is_valid = validate_email(email)
is_valid
if(is_valid==True):
    print("Email Verified!")
else:
    print("Enter a correct email ")

Email = input("Enter your email again.")  
is_valid = validate_email(Email)
is_valid
is_valid = validate_email(Email,check_mx=True)
is_valid
is_valid = validate_email(Email,verify=True)
is_valid
if(is_valid==True):
    print("Email Verified!")
else:
    print("Enter a correct email ")
    input("Enter your email again.")
    
