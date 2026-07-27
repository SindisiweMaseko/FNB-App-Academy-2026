"""
Project: The Concert Ticket Booker
Description: A simple digital ticket counter that collects user 
             information and outputs a personalized booking confirmation.
"""

def book_tickets():
    print("--- Welcome to the Concert Ticket Booker ---")
    
    # 1. Ask the user for their name
    name = input("Enter your name: ").strip()
    
    # 2. Ask them for the name of the band/artist they want to see
    artist = input("Enter the name of the band or artist you want to see: ").strip()
    
    # 3. Print a personalized confirmation message using an f-string
    print(f"\nHey {name}! Your tickets to see {artist} are booked successfully!")

if __name__ == "__main__":
    book_tickets()