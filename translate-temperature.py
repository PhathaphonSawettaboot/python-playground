def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5)+32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

choice = input("Choose conversion:\n1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\nEnter choice (1/2) :")

if choice == '1':
    celsius = float(input("Enter temperature in Celcius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")

elif choice == '2':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = celsius_to_fahrenheit(fahrenheit)
    print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
else:
    print("Invalid choice")