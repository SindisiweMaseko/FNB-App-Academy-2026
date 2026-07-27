"""
 Challenge 2: The Secure Password Hint Tool
 Description: A simple tool that collects a user's password and provides a hint for it.
"""

def password_hint_tool():
    # 1. Ask the user to input their secret password
    password = input("Enter your secret password: ")

    # 2. Use .strip() to clean up any accidental spaces at the start or end
    clean_password = password.strip()

    # 3. Grab the very first letter and the very last letter using string indexing
    first_letter = clean_password[0]
    last_letter = clean_password[-1]

    # 4. Print a hint using an f-string with uppercase formatting
    print(f"Your password hint: It starts with {first_letter.upper()} and ends with {last_letter.upper()}")

if __name__ == "__main__":
    password_hint_tool()