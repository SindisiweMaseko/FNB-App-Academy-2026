"""
Project: The Phone Directory Search
Description: A mini data directory using a dictionary to look up friend phone numbers.
"""

contacts = {
    "Alice": "0821112222",
    "Bob": "0833334444",
    "Charlie": "0845556666"
}

search_name = input("Enter the name of the friend you want to look up: ")

if search_name in contacts:
    print(f"Found! {search_name}'s number is {contacts[search_name]}")
else:
    print("Contact not found.")