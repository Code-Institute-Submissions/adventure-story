"""
This first section will hold the first print and input statements, welcoming the player to the game
"""
print("Welcome to Adventure Stories! \n Forest edition. \n")
print("Rules of the game: \n")
print("1. You have to be 18+ to play this game. \n")
print("\n 2. You can only type an that is given to you.")
print("\n If you type anything else your story will be over!")
age = int(input("Please type your age here "))
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
                go_home_or_go_right = input("\n You are now back to where you started,\n do you want to go back home or the right? (home/right)").lower()
                if go_home_or_go_right == "home":
                    print("Have some rest and try again. \n GAME OVER")
                elif go_home_or_go_right == "right":
                    ignore_or_leave = input("You hear a weird noise, do you carry on and ignore the noise or leave? \n (ignore/leave)").lower()
                    if ignore_or_leave == "ignore":
                        print("You start to hear howling, oh no its too late! You get surrounded by wolfs! \n GAME OVER")
                    elif ignore_or_leave == "leave":
                        print("You decided to leave and go home, have some rest and try again. \n GAME OVER")
                    else:
                        print("Uh oh, that wasn't an available answer. \n GAME OVER!")
                else:
                    print("Uh oh, that wasn't an available answer. \n GAME OVER!")
            else:
                print("Uh oh, that wasn't an available answer. \n GAME OVER!")
        elif left_or_right == "right":
            """
            Second question (after player decided to go right), they hear a weird noise, do they explore or go home?
            """
            explore_or_go_home = input("You hear a weird noise, do you carry on and investigate the noise or go home? \n (investigate/go home)").lower()
            if explore_or_go_home == "investigate":
                print("You get surrounded by wolfs! \n GAME OVER")
            elif explore_or_go_home == "go home":
                print("Have some rest and try again. \n GAME OVER")
            else:
                print("Uh oh, that wasn't an available answer. \n GAME OVER!")
        else:
            print("Uh oh, that wasn't an available answer. \n GAME OVER!")
            """
            Player has selected to wait until morning.
            """
    elif day_or_night == "wait":
            """
            Second question, do they go to the lake or the hill?
            """
            lake_or_hill = input("You reach two paths, the left one will lead you to a lake, the right will take you to a hill. \n Where fo you want to go? (lake/hill)").lower()
            if lake_or_hill == "lake":
                """
                3rd question, you see a boat do you go in it?
                """
                hut_or_boat = input("You finally get to the lake, you see a hut on your left and a small boat in the lake. \n Do you explore the hut or take the boat for a ride? (hut/boat)")
                if hut_or_boat == "hut":
                    print("As you aproach, you see what looks likes human remains sticking out of the ground. \n You get scared and run home. \n GAME OVER!")
                elif hut_or_boat == "boat":
                    print("You get halfway into the lake when you notice you've been taking on water through a small hole. \n You try to block the hole but it gets worse. \n The boat starts to sink and you can't swim. \n GAME OVER!")
                else:
                    print("Uh oh, that wasn't an available answer. \n GAME OVER!")
            elif lake_or_hill == "hill":
                print("Before you make it to the hill you get surrounded by wolfs! \n GAME OVER")
            else:
                print("Uh oh, that wasn't an available answer. \n GAME OVER!")
    else:
        print("Uh oh, that wasn't an available answer. \n GAME OVER!")
"""
This statement will check to see whether the age that is entered is either equal to 18 or is older.
If this is the case, the game will run.
if not then the game will end.
"""
if age >= 18:
    forestAdventureGame()
else:
    print("Sorry you have to be atleast 18 to play this game.")
