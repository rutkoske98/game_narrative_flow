import random

# Define the rooms and their descriptions
rooms = {
    "kitchen": """
          __
    .----|  |_
   /  /  / / /
  /  (  /_/ /
 /_________/\\
(___________)
    """,
    "living room": """
        _______
       /      /,
      /      //
     /______//
    (______(/
    """,
    "bedroom": """
     __  _
    /  \( )_
    ) D (/  )
   (  C  /__
   / /\_// /\\
  / / /\/ / /
 / / /   / /
 \ \ \__/_/
  \_\)
    """,
    "mudroom": """
  __________
 |  ______  |
 | |      | |
 | |      | |
 | |______| |
 |__________|
    """,
    "basement": """
  _______________
 /               \\
/                 \\
|     _____       |
|    |_____|      |
|                 |
|_________________|
    """,
    "attic": """
     _________
    /   /   /\\
   /___/___/  \\
  |   /   /\\   |
  |__/___/__\\__|
     |       |
     |_______|
    """
}

# Define the possible outcomes for each room
outcomes = {
    "kitchen": "You find your teddy bear hiding behind the cookie jar!",
    "living room": "You find an imp playing with your teddy bear!",
    "bedroom": "You find your teddy bear tucked safely under your pillow.",
    "mudroom": "You find your teddy bear tangled in your raincoat.",
    "basement": "You find your teddy bear sitting among old boxes.",
    "attic": "You find your teddy bear sitting among dusty old toys."
}

# Define the imps and their actions
imps = {
    "kitchen": "You catch a glimpse of a mischievous imp darting behind the refrigerator.",
    "living room": "You hear giggling from behind the couch, but when you look, there's no one there.",
    "bedroom": "You notice a small figure disappear under your bed.",
    "mudroom": "You see a shadow dart behind the coat rack.",
    "basement": "You hear strange noises coming from the dark corners of the room.",
    "attic": "You notice objects shifting in the dim light of the attic."
}

# Function to prompt the user for a room choice
def choose_room(choices):
    print("Which room do you want to search?")
    for i, room in enumerate(choices, 1):
        print(f"{i}. {room}")
    choice = input("Enter the number of your choice: ")
    return choices[int(choice) - 1]

# Function to play the game
def play_game():
    print("Welcome to Anna's Adventure!")
    print("Anna is searching for her lost teddy bear.")
    print("Let's help her find it!")
    found = False
    choices = ["living room", "kitchen"]
    for i in range(3):
        if i == 1:
            choices = ["bedroom", "attic"]
        elif i == 2:
            choices = ["mudroom", "basement"]
        room = choose_room(choices)
        print(rooms[room])
        print(imps[room])
        action = input("What do you want to do? (1. Search the room, 2. Move to another room): ")
        if action == "1":
            print(outcomes[room])
            if room == "living room":
                print("Oh no! You found an imp playing with your teddy bear!")
                print("Anna tries to catch the imp, but it disappears in a puff of smoke.")
                print("Better luck next time!")
            else:
                print("Congratulations! You found your teddy bear!")
                found = True
                break
        else:
            print("You decide to search another room.")
    if not found:
        print("You couldn't find your teddy bear. Maybe next time!")

# Call the play_game function to start the game
play_game()
