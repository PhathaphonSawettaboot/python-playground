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


