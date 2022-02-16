"""
This first section will hold the first print and input statements, welcoming the player to the game
"""

print("Welcome to Adventure Stories! \n")

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
    day_or_night = input( "you are ready to enter the forest, but its almost night, \n do you still go or do they wait until morning? (go now/wait) \n").lower()
    """
    Player has selected to go at night
    """
    if day_or_night == "go now":
        """
        Second question, do they go left or right?
        """
        left_or_right = input("\n There are 2 paths ahead. \n But it is to dark to read the signs, do you take the left or right path? (left/right)").lower()
        if left_or_right == "left":
            
            """
            Third Question, do they go to the house or not? go_or_no_go
            """
            go_or_no_go = input("\n You have gone down the left path and see a small hut with lights on up ahead, do you go to it or go back to where you came from? (go/turn back)").lower() 
            
            """
            Player has decied to go towards the hut. This ends the Story!
            """
            if go_or_no_go == "go":
                print("\n A man stepped out of the hut with a knife, you ran away. \n GAME OVER")

                """
                Player has decied to turn back.
                """
            elif go_or_no_go == "turn back":

                """
                Player gets back to the 2 paths, do they take the go home or go right?
                """
                go_home_or_go_right = input("\n You are now back to where you started,\n do you want to go back home or the right? (home/right)")
                if go_home_or_go_right == "home":
                    print("Have some rest and try again. \n GAME OVER")

                elif go_home_or_go_right == "right":

                else:
                print("Uh oh, that wasn't an available answer. \n GAME OVER!")
                """
                Player has entered an incorrect answer, end's the game.
                """
            else:
                print("Uh oh, that wasn't an available answer. \n GAME OVER!")

        elif left_or_right == "right":
            """
            Second question (after player decided to go right), they hear a weird noise, do they explore or go home?
            """
            explore_or_go_home = input("You hear a weird noise, do you carry on and investigate the noise or go home? \n (investigate/go home)")
            
            if explore_or_go_home == "investigate":
                print("You get surrounded by wolfs! \n GAME OVER")

            elif explore_or_go_home == "go home":
                print("Have some rest and try again. \n GAME OVER")

            else:
                print("Uh oh, that wasn't an available answer. \n GAME OVER!"
            
        else:
            print("Uh oh, that wasn't an available answer. \n GAME OVER!")

        """
        Player has selected to wait until morning.
        """
    elif day_or_night == "wait":
        """
        Second question, do they go ?
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
    forestAdventureGame()
elif selectedStory == "city":
    cityAdventureGame()
else:
    print("It doesnt look like that game exists. \n Please start again.")
    
    









forestAdventureGame()
cityAdventureGame()