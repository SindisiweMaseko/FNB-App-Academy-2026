"""
Challenge 4: Smart ATM
"""

def smart_atm():
    # 1. Set a fixed variable representing a bank balance
    balance = 500

    # 2. Ask the user how much money they want to withdraw and cast it to a float
    withdrawal_amount = float(input("Enter the amount you want to withdraw: R"))

    # 3. Check if the request is less than or equal to 0 (Invalid amount)
    if withdrawal_amount <= 0:
        print("Invalid amount. You must withdraw more than R0")

    # 4. Check if the request is less than or equal to the balance (Successful withdrawal)
    elif withdrawal_amount <= balance:
        balance -= withdrawal_amount
        print(f"Withdrawal successful! Remaining balance: R{balance}")

    # 5. Otherwise, the request is greater than the balance (Insufficient funds)
    else:
        print("Declined. Insufficient funds")


if __name__ == "__main__":
    smart_atm()