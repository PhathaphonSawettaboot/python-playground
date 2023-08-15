"""
manage a list of names.
This program focuses on using different modes to read,
write, and append data to a file.
"""
def write_names(names):
    with open('names.txt', 'w') as file:
        for name in names:
            file.write(name + '\n')

def read_names():
    try:
        with open('names.txt', 'r') as file:
            names = file.readlines()
            names = [name.strip() for name in names]
            return names
    except FileNotFoundError:
        print("File 'names.txt' not found.")
        return []

def append_name(name):
    with open('names.txt', 'a') as file:
        file.write(name + '\n')

names = ['Alice' , 'Bob' , 'Charlie' , 'David']

write_names(names)

while True:
    print("Select an action:")
    print("1. Add Name")
    print("2. Views Names")
    print("3. Quit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        new_name = input("Enter a new name: ")
        append_name(new_name)
        print(f"Added '{new_name} to the list.")
    elif choice == 2:
        names = read_names()
        if names:
            print("Names in the list:")
            for idx, name in enumerate(names, start=1):
                print(f"{idx}. {name}")
        else:
            print("The list is empty.")
    elif choice == 3:
        print("Existing the program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")