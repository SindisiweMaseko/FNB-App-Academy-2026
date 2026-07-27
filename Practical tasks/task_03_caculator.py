"""
Practical task 03: 
Description: Takes two numbers as input and performs all four basic arithmetic 
             operations plus two advanced operations with rounded outputs and error handling.
"""

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

addition = round(num1 + num2, 2)
subtraction = round(num1 - num2, 2)
multiplication = round(num1 * num2, 2)

if num2 != 0:
    division = round(num1 / num2, 2)
    floor_div = round(num1 // num2, 2)
    modulus = round(num1 % num2, 2)
    div_result = f"{division}"
    floor_result = f"{floor_div}"
    mod_result = f"{modulus}"
else:
    div_result = "Error: Division by zero"
    floor_result = "Error: Division by zero"
    mod_result = "Error: Division by zero"

print(f"\n--- Calculator Results ---")
print(f"{'Operation':<20} | {'Result':<10}")
print("-" * 35)
print(f"{'Addition':<20} | {addition:<10}")
print(f"{'Subtraction':<20} | {subtraction:<10}")
print(f"{'Multiplication':<20} | {multiplication:<10}")
print(f"{'Division':<20} | {div_result:<10}")
print(f"{'Floor Division':<20} | {floor_result:<10}")
print(f"{'Modulus':<20} | {mod_result:<10}")