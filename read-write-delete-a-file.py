"""
cd ~/Documents
python3 read-write-delete-a-file.py
"""

#Reading
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

#Writing
with open('example.txt', 'w') as file:
    file.write('Hellp, this is a new line.\n')
    file.write('And here is another line. \n')

#Appending
with open('example.txt', 'a') as file:
    file.write('This is appended.\n')