"""
This first section will hold the first print and input statements, welcoming the player to the game
"""

print("Welcome to Adventure Stories! \n")
characterName = input("What would you like your characters name to be? \n")

print("Rules of the game: \n")
print("There is only one rule, you can only type an that is given to you. \n If you type anything else your story will be over!")

print("Which story would you like to play? \n Forrest or City") 
selectedStory = input("Please type the name of the story you want to play. ").lower()

"""
This is the function that will hold the forrest adventure story line
"""
def forrestAdventureGame():
    print("Welcome to the forrest story.\n")

    """
    This will be the first question in the story.
    """
    day_or_night = input("You are ready to enter the forrest, but its almost night, \n do you still go or do you wait until morning? (go now/wait) ").lower()
    if day_or_night == "go now":
        print("night")
    elif day_or_night == "wait":
        print("morning")
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

if selectedStory == "forrest":
    forrestAdventureGame()
elif selectedStory == "city":
    cityAdventureGame()
else:
    print("It doesnt look like that game exists. \n Please start again.")
    
    









# forrestAdventureGame()
# cityAdventureGame()