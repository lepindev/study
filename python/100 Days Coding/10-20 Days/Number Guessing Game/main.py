import art
import random
print(art.logo)

end = False

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

numbers = []
for i in range(1, 101):
	numbers.append(i)
	
guess = random.choice(numbers)
print(f"pss, the correct answer is {guess}")

user_input = input("Choose a difficulty. Type 'easy' or 'hard':")

attempts = 10
while attempts != 0:
	if user_input == "easy":
		print(f"You have {attempts} attempts")
		make_guess = int(input("Make a guess: "))
		if make_guess == guess:
			print("You win!")
			break
		else:
			if attempts == 0:
				print("You lose")
				break
			if make_guess > guess:
				print("Too much")
			else:
				print("Too low")
	elif user_input == "hard":
		print(f"You have {attempts - 5} attempts")
		make_guess = int(input("Make a guess: "))
		if make_guess == guess:
			print("You win!")
			break
		else:
			attempts -= 1
			if attempts - 5 == 0:
				print("You lose")
				break
			if make_guess > guess:
				print("Too much")
			else:
				print("Too low")
			
	
	else:
		print("Print a correct one: 'easy' or 'hard'")
		print("Please restart")
		break
		
		
