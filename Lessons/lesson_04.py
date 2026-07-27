"""
lesson_04: 
Description: A security checker script that uses control flow (if, elif, and else statements) 
             alongside logical operators to manage establishment and VIP access based on age and ticket status.
"""


#Basic if/else statements
age = int(input("Enter your age: "))
section_pass = input("Do you have a VIP ticket? (yes/no)").lower()

if age >= 21 and section_pass == "yes":
    print("Access Granted to VIP Section !")
elif age >= 21:
    print("Access Granted to General Section !")
else:
    print("Access Denied !!!")