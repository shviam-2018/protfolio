email = input("Enter email: ").strip()

username, domain = email.split('@')

if domain == "gmail.com":
    domain = "Google Mail - default domain"
else:
    domain = str(domain) + " - business domain"

print(f"Your username is {username} and domain is {domain}")
