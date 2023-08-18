# Email Validation
import re

email = "la-la@email.com"
if re.match(r'^[\w\.-]+@[\w\.-]+$', email):
    print("Valid email")
else:
    print("Invalid email")

#URL Detection
import re
text = "Visit my website at https://www.example.com"
urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
print(urls)

#Phone Number Validation
phone = "123-456-7890"
if re.match(r'^\d{3}-\d{3}-\d{4}$', phone):
    print("Valid Phone Number")
else:
    print("Invalid Phone Number")

#Data Extraction
text = "Date: 2023-07-31"
date = re.search(r'\d{4}-\d{2}-\d{2}', text).group()
print(date)


import re
text = "Hello, world!"
new_text = re.sub(r'world', 'Python', text)
print(new_text)


import re
text = "  Hello    there  "
clean_text = re.sub(r'\s+', ' ', text).strip()
print(clean_text)


import re
text = "Hello! How's it going?"
clean_text = re.sub(r'[^\w\s]', '', text)
print(clean_text)


import re
password = "Passw0rd!"
if re.match(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$', password):
    print("Valid password")
else:
    print("Invalid password")


import re
ip = "192.168.1.1"
if re.match(r'^(\d{1,3}\.){3}\d{1,3}$', ip):
    print("Valid IP address")
else:
    print("Invalid IP address")


import re
credit_card = "1234-5678-9012-3456"
masked_card = re.sub(r'\d{4}-\d{4}-\d{4}', '****-****-****-****', credit_card)
print(masked_card)