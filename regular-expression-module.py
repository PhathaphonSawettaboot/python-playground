import re

email = "la-la@email.com"
if re.match(r'^[\w\.-]+@[\w\.-]+$', email):
    print("Valid email")
else:
    print("Invalid email")