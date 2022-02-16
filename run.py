"""
This first section will hold the first print
and input statements, welcoming the player to the game
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
    print("you are ready to enter the forest, but its almost night, ")
    print("\n do you still go or do they wait until morning?")
    day_or_night = input("(go now/wait) \n").lower()
    """
    Player has selected to go at night
    """
    if day_or_night == "go now":
        """
        Second question, do they go left or right?
        """
        print("\n There are 2 paths ahead. But it is to dark to read")
        print("\n the signs, do you take the left or right path? ")
        left_or_right = input("\n (left/right)").lower()
        if left_or_right == "left":
            """
            Third Question, do they go to the house or not? go_or_no_go
            """
            print("\n You have gone down the left path and see a small")
            print("hut with lights on up ahead,")
            print("do you go to it or go back to where you came from?")
            go_or_no_go = input("\n (go/turn back)").lower()
            """
            Player has decied to go towards the hut. This ends the Story!
            """
            if go_or_no_go == "go":
                print("\n A man stepped out of the hut with a knife,")
                print(" you ran away. \n GAME OVER")
                """
                Player has decied to turn back.
                """
            elif go_or_no_go == "turn back":
                """
                Player gets back to the 2 paths,
                do they take the go home or go right?
                """
                print("\n You are now back to where you started,")
                print("\n do you want to go back home or the right?")
                go_home_or_go_right = input("\n (home/right)").lower()
                if go_home_or_go_right == "home":
                    print("Have some rest and try again. \n GAME OVER")
                elif go_home_or_go_right == "right":
                    print("You hear a weird noise, do you")
                    print(" carry on and ignore the noise or leave?")
                    ignore_or_leave = input("\n (ignore/leave)").lower()
                    if ignore_or_leave == "ignore":
                        print("You start to hear howling, oh no its ")
                        print("too late! You get surrounded by wolfs!")
                        print("\n GAME OVER")
                    elif ignore_or_leave == "leave":
                        print("You decided to leave and go home, ")
                        print("have some rest and try again.")
                        print("\n GAME OVER")
                    else:
                        print("Uh oh, that wasn't an available answer.")
                        print("\n GAME OVER!")
                else:
                    print("Uh oh, that wasn't an available answer. ")
                    print("\n GAME OVER!")
            else:
                print("Uh oh, that wasn't an available answer.")
                print("\n GAME OVER!")
        elif left_or_right == "right":
            """
            Second question (after player decided to go right),
            they hear a weird noise, do they explore or go home?
            """
            print("You hear a weird noise, do you")
            print(" carry on and investigate the noise")
            print(" or go home? ")
            explore_or_go_home = input("\n (investigate/go home)").lower()
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
            print("You reach two paths,")
            print(" the left one will lead you to a lake,")
            print(" the right will take you to a hill.")
            print("\n Where fo you want to go?")
            lake_or_hill = input("(lake/hill)").lower()
            if lake_or_hill == "lake":
                """
                3rd question, you see a boat do you go in it?
                """
                print("You finally get to the lake, ")
                print("you see a hut on your left ")
                print("and a small boat in the lake.")
                print("\n Do you explore the hut ")
                print("or take the boat for a ride?")
                hut_or_boat = input("(hut/boat)")
                if hut_or_boat == "hut":
                    print("As you aproach, you see what looks like ")
                    print("human remains sticking out of the ground.")
                    print("\n You get scared and run home.")
                    print("\n GAME OVER!")
                elif hut_or_boat == "boat":
                    print("You get halfway into the lake when you ")
                    print("notice you've been taking on water ")
                    print("through a small hole.")
                    print("\n You try to block the hole but it gets worse.")
                    print("\n The boat starts to sink and you can't swim.")
                    print("\n GAME OVER!")
                else:
                    print("Uh oh, that wasn't an available answer.")
                    print("\n GAME OVER!")
            elif lake_or_hill == "hill":
                print("Before you make it to the hill you ")
                print("get surrounded by wolfs!")
                print("\n GAME OVER")
            else:
                print("Uh oh, that wasn't an available answer.")
                print("\n GAME OVER!")
    else:
        print("Uh oh, that wasn't an available answer.")
        print("\n GAME OVER!")
"""
This statement will check to see whether the age
that is entered is either equal to 18 or is older.
If this is the case, the game will run.
if not then the game will end.
"""
if age >= 18:
    forestAdventureGame()
else:
    print("Sorry you have to be atleast 18 to play this game.")
