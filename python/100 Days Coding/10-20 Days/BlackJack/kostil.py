import random
import logo
import replit


def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    score = 0
    for i in cards:
        score += i
    return score


def compare(user_score, computer_score):
    if user_score < 22:
        if user_score == 21 and computer_score == 21:
            return 1
        elif user_score > computer_score:
            return 2
        elif computer_score > 21:
            return 3
    else:
        return 5


end = False


def blackjack_game():
    user_score = 0
    computer_score = 0
    your_cards = []
    your_cards.append(deal_cards())
    your_cards.append(deal_cards())
    user_score += calculate_score(your_cards)
    computer_cards = []
    while computer_cards != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score += calculate_score(computer_cards)
    while True:
        print(f"Your card are {your_cards}")
        print(f"Computer's first card: {computer_cards[0]}")
        if input("Do you want a new card? y/N: ") == "y":
            your_cards.append(deal_cards())
            user_score += calculate_score(your_cards)
            if compare(user_score, computer_score) == 1:
                print(f"Your score = {user_score}")
                print(f"Computer score = {computer_score}")
                print("Draw")
                break
            elif compare(user_score, computer_score) == 2:
                print(f"Your score = {user_score}")
                print(f"Computer score = {computer_score}")
                print("You win")
                break
            elif compare(user_score, computer_score) == 3:
                print(f"Your score = {user_score}")
                print(f"Computer score = {computer_score}")
                print("You win")
                break
            else:
                print(f"Your score = {user_score}")
                print(f"computer_score = {computer_score}")
                print("You lose")
                break
        else:
            if compare(user_score, computer_score) == 1:
                print(f"Your score = {user_score}")
                print(f"Computer score = {computer_score}")
                print("Draw")
                break
            elif compare(user_score, computer_score) == 2:
                print(f"Your score = {user_score}")
                print(f"Computer score = {computer_score}")
                print("You win")
                break
            elif compare(user_score, computer_score) == 3:
                print(f"Your score = {user_score}")
                print(f"Computer score = {computer_score}")
                print("You win")
                break
            else:
                print(f"Your score = {user_score}")
                print(f"computer_score = {computer_score}")
                print("You lose")
                break
            break


while not end:
    if input("Do you want to play blackjack? Type 'y' or 'n': ") == "y":
        print(logo.logo)
        blackjack_game()
    else:
        print("Bye")
        end = True
