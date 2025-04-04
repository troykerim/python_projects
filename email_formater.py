# Email Converter

import re 
email = input("Enter your email: ")
delimiters = r"[@.]"
result = re.split(delimiters, email)
print(result)

'''
email2 = input("Enter your email: ").strip()
username = email2[:email.index("@")]
domain_name = email2[email.index("@")+1:]
formater = (f"Your user name is '{username}' and your domain is '{domain_name}'")
print(formater)'''
