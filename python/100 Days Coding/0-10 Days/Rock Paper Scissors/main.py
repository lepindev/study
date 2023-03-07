import random

import rps_module

userInput = input(
    "Wagwan, what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "
)
result = ""
userInput = int(userInput)
print("Your chose:")
if userInput > 2 or userInput < 0:
    print("Error")
elif userInput == 0:
    print(rps_module.rock)
elif userInput == 1:
    print(rps_module.paper)
else:
    print(rps_module.scissors)

print("Computer Choise:")
randomChoise = random.randint(0, 2)
if randomChoise == 0:
    print(rps_module.rock)
elif randomChoise == 1:
    print(rps_module.paper)
else:
    print(rps_module.scissors)

print("RESULT:")
if userInput > 2 or userInput < 0:
    print("Error")
elif userInput == randomChoise:
    print("Draw")
elif (
    userInput == 0
    and randomChoise == 1
    or userInput == 1
    and randomChoise == 2
    or userInput == 2
    and randomChoise == 0
):
    print("You lose")
else:
    print("You win")
