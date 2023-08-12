even_numbers = []
odd_numbers = []

while True:
    try:
        num = int(input("Enter a number (0 to quit): "))
        if num == 0:
            break
        elif num % 2 == 0:
            even_numbers.append(num)
            print("\nEven numbers:" , even_numbers)
        else:
            odd_numbers.append(num)
            print("\nOdd numbers: ", odd_numbers)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print("\nEven numbers:" , even_numbers)
print("Odd numbers: ", odd_numbers)