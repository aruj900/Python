print("Welcome to Treasure Island, your mission is to find treasure")

turn = input("You are at the crossroad will you left of right? ")
turn = turn.lower()
if turn == "left":
    water = input("you are at water bank will you wait for boat or swim? ")
    water = water.lower()
    if water == "wait":
        door = input("There are three doors red, blue and yellow, which door will your choose? ")
        door = door.lower()
        if door == "yellow":
            print("You Win!!")
        else:
            print("Game Over!!")
    
    else:
        print("Game over, sharks ate you")

else:
    print("Game Over you fell")