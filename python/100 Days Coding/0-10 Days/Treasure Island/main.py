print("Project 3")
print("==================")
print("Welcome to Treasure Island.\nYour mission to find the treasure.")
side = input("left or right?")
if side.lower() == "left":
    swimOrWait = input("Swim or Wait?")
    if swimOrWait.lower() == "wait":
        door = input("Which door? Blue or Red or Yellow?")
        if door.lower() == "red":
            print("Burned by fire.\nGame Over.")
        elif door.lower() == "blue":
            print("Eaten by beasts\nGame Over.")
        elif door.lower() == "yellow":
            print("You Win!")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout.\nGame Over.")
else:
    print("Fall into a hole.\nGame Over.")

