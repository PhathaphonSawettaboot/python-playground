def main():
    numbers = get_numbers_from_user()
    operations = get_operation_choices()

    if 'sum' in operations:
        result = calculate_sum(numbers)
        print(f"The sum of the numbers is: {result}")

    if 'avg' in operations:
        result = calculate_avg(numbers)
        print(f"The average of the numbers is: {result:.2f}")

    if 'min' in operations:
        result = calculate_min(numbers)
        print(f"The minimum number is: {result}")
    
    if 'max' in operations:
        result = calculate_max(numbers)
        print(f"The maximum number is: {result}")


def get_numbers_from_user():
    input_string = input("Enter numbers seperated by comma: ")
    number_strings = input_string.split(',')
    numbers = [float(num) for num in number_strings]
    return numbers

def get_operation_choices():
    choices = input("Choose operations ('sum' , 'avg' , 'min' , 'max') seperated by commas: ")
    return [choice.strip().lower() for choice in choices.split(',')]

def calculate_sum(numbers):
    return sum(numbers)

def calculate_avg(numbers):
    return sum(numbers)/ len(numbers)

def calculate_min(numbers):
    return min(numbers)

def calculate_max(numbers):
    return max(numbers)

if __name__ == "__main__":
    main()