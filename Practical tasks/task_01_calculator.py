"""
Practical task 01:  Student Info Formatter
Description: Collects personal information from the user and displays it in a formatted profile card.
"""

first_name = input("Enter your first name: ")
surname = input("Enter your surname: ")
age = int(input("Enter your age: "))
fav_number = float(input("Enter your favourite number: "))

full_name = f"{first_name} {surname}"

print(f"Welcome, {full_name}!")
print(f"Uppercase Name: {full_name.upper()}")
print(f"Title Case Name: {full_name.title()}")
print(f"Age in months: {age * 12}")
print(f"Rounded favourite number: {round(fav_number, 2)}")
print(f"Data type of first_name: {type(first_name)}")
print(f"Data type of surname: {type(surname)}")
print(f"Data type of age: {type(age)}")
print(f"Data type of fav_number: {type(fav_number)}")