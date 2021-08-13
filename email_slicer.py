email_address = input("Please enter your email address: ").strip()
username = email_address[:email_address.index("@")]
domain_name = email_address[email_address.index("@") + 1:]
result = (f"Your user name is '{username}', and your domain name is '{domain_name}'")
print(result)