# Get user input for the amount to exchange
amount = int(input("Enter the amount in baht: "))

# List of available folding and coin denominations
denominations = [1000, 500, 100, 50, 20, 10, 5, 2, 1]

# Initialize a dictionary to store the result
result = {}

# Iterate through each denomination
for denomination in denominations:
    if amount >= denomination:
        count = amount // denomination
        result[denomination] = count
        amount = amount - count * denomination

# Display the result
print("Return the following:")
for denomination, count in result.items():
    print(f"{count} x {denomination} baht")