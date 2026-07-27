"""
Challenge 3: The Advanced Password Validator
Description: The South African Fuel Cost Calculator
"""

def password_validator():
    # 1. Ask the user how many kilometers they want to drive
    kilometers = float(input("Enter the number of kilometers you want to drive: "))

    # 2. Ask them for the current petrol price per liter
    petrol_price = float(input("Enter the current petrol price per liter (e.g., 22.45): "))

    # 3. Calculate liters needed (1 liter for every 10 kilometers)
    liters_needed = kilometers / 10

    # 4 & 5. Calculate total cost and format it to 2 decimal places using round()
    total_cost = round(liters_needed * petrol_price, 2)

    # Print the final cost result
    print(f"Total estimated fuel cost: R{total_cost}")


if __name__ == "__main__":
    password_validator()
