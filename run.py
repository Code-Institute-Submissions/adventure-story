"""
This first section will hold the first print and input statements, welcoming the player to the game
"""

print("Welcome to Adventure Stories! \n")
characterName = input("What would you like your characters name to be? \n")
print("Which story would you like to play? \n Forrest or City") 

selectedStory = input("Please type the name of the story you want to play. ").lower()

"""
This if statement will check to see what story has been selected.
"""

if selectedStory == "forrest":
    print(2)
else:
    print(3)






# forrestAdventureGame = print(2)

# cityAdventureGame = print(3)


# forrestAdventureGame()
# cityAdventureGame()