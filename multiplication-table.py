num = int(input("Multiplication Table for: "))

print(f"Multiplication Table for {num} :")
for i in range(1,13):
    result = num * i
    print(f"{num} x {i} = {result}")