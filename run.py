"""
This first section will hold the first print and input statements, welcoming the player to the game
"""

print("Welcome to Adventure Stories! \n")
characterName = input("What would you like your characters name to be? \n")

print("Rules of the game: \n")
print("There is only one rule, you can only type an that is given to you. \n If you type anything else your story will be over!")

print("Which story would you like to play? \n Forest or City") 
selectedStory = input("Please type the name of the story you want to play. ").lower()

"""
This is the function that will hold the forrest adventure story line
"""
def forestAdventureGame():
    print("Welcome to the forest story.\n")

    """
    This will be the first question in the story.
    """
    day_or_night = input(characterName "is ready to enter the forest, but its almost night, \n do they still go or do they wait until morning? (go now/wait) ").lower()
    """
    Player has selected to go at night
    """
    if day_or_night == "go now":
        """
        Second question, do they go left or right?
        """
        left_or_right = input(characterName "has just got to the forest, there are 2 paths. \n But it is to dark to read the signs, do they take the left or right path? (left/right)").lower()
        if left_or_right == "left":
            print("woo")
        elif left_or_right == "right":
            print("ooo")
        else:
        print("Uh oh, that wasn't an available answer. \n GAME OVER!")

    """
    Player has selected to wait until morning.
    """
    elif day_or_night == "wait":
        """
        Second question, do they go left or right?
        """

    """
    Player has entered an incorrect answer, end's the game.
    """
    else:
        print("Uh oh, that wasn't an available answer. \n GAME OVER!")


"""
This is the function that will hold the city adventure story line
"""
def cityAdventureGame():
    print("You are now in the c game")

"""
This if statement will check to see what story has been selected.
"""

if selectedStory == "forest":
    forrestAdventureGame()
elif selectedStory == "city":
    cityAdventureGame()
else:
    print("It doesnt look like that game exists. \n Please start again.")
    
    









# forrestAdventureGame()
# cityAdventureGame()