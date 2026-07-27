"""
Practical task 02:Username and Message Formatter  
Description: Takes a user's first name, last name, and a short bio message as input, 
             then applies multiple string transformations to produce a formatted user profile output.
"""

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
bio_message = input("Enter your short bio message: ")

username = f"{first_name[0]}{last_name}".lower()
full_name = f"{first_name} {last_name}"
clean_bio = bio_message.strip().replace("I am", "I'm")
bio_length = len(clean_bio)

print(f"\n--- User Profile Output ---")
print(f"Username: {username}")
print(f"Full Name: {full_name.title()}")
print(f"Bio: {clean_bio}")
print(f"Character Count: {bio_length}")