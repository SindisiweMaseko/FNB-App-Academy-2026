"""
Project: The High-Score Tracker Game
Description: An interactive program that continuously asks an arcade player for their game score.
"""

while True:
    score_input = input("Enter a game score: ")
    
    if score_input.strip().lower() == "stop":
        print("Game session ended!")
        break
    else:
        score = int(score_input)
        if score > 100:
            print("Wow! That's a new high score!")
        else:
            print("Good try, keep playing!")