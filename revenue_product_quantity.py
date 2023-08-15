import csv

def analyze_sales(filename):
    total_revenue = 0
    product_counts = {}

    with open(filename, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            product = row['Product']
            quantity = int(row['Quantity'])
            price = float(row['Price'])

            revenue = quantity * price
            total_revenue = total_revenue + revenue

            """
            Checks if the value of the variable product
            (which represents the name of a product from a row in the CSV file)
            is already a key in the product_counts dictionary.
            - If the product is already in the dictionary,
            the condition evaluates to True.
            """

            if product in product_counts:
                product_counts[product] = product_counts[product] + quantity
            else:
                product_counts[product] = quantity
    
    print("Sales Analysis:")
    print(f"Totalrevenue: ${total_revenue:.2f} ")
    print("Product quantities:")
    for product, quantity in product_counts.items():
        print(f"{product}: {quantity} units")

analyze_sales('sales.csv')