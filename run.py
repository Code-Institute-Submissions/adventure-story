def restartTheGame():
    

"""
This first section will hold the first print and input statements, welcoming the player to the game
"""

print("Welcome to Adventure Stories! \n")
characterName = input("What would you like your characters name to be? \n")
print("Which story would you like to play? \n Forrest or City") 

selectedStory = input("Please type the name of the story you want to play. ").lower()

"""
This is the function that will hold the forrest adventure story line
"""
def forrestAdventureGame():
    print("You are now in the f game")

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
    print("It doesnt look like that game exists. \n Please enter either Forrest or City")
    selectedStory = input("Please type the name of the story you want to play. ").lower()






# forrestAdventureGame = print(2)

# cityAdventureGame = print(3)


# forrestAdventureGame()
# cityAdventureGame()