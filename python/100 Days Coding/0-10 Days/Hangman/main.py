import random

import hangman_arts
import replit

print(hangman_arts.logo)
print(hangman_arts.stages[6])
fruits = ["banana", "peach", "apple", "watermelon", "melon", "pear"]
random_fruit = random.choice(fruits)

blanks = []
for i in range(len(random_fruit)):
    blanks += "_"

lives = 6
result = False

while not result:
    guess = input("Guess the letter:")
    replit.clear()
    for i in range(len(random_fruit)):
        letter = random_fruit[i]
        if letter == guess:
            blanks[i] = letter
    print(f"{' '.join(blanks)}")

    if guess not in random_fruit:
        lives -= 1
        print(f"Lives: {lives}")
        if lives == 0:
            print("You lost")
            result = True
    if "_" not in blanks:
        print("You win")
        result = True
    print(hangman_arts.stages[lives])
