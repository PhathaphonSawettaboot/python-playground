def calculate_bmi(weight , height):
    bmi = weight / (height ** 2)
    return bmi

def bmi_status(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

weight = float(input("Enter yout weight in kilograms: "))
height = float(input("Enyter your height in meters: "))

bmi = calculate_bmi(weight, height)
status = bmi_status(bmi)
print(f"Your BMI is: {bmi:.3f}")
print(f"Your BMI status is: {status}")