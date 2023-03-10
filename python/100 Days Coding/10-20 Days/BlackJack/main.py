import random
import logo
import replit


def random_cards():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card


def compare(user_score, computer_score):
    if user_score <= 21:
        if computer_score > 21:
            return "You win"
        elif user_score > computer_score:
            return "You win"
        elif user_score == computer_score:
            return "Draw"
        else:
            return "You lose"
    else:
        return "You lose"
    return ""


def calculation_score(cards):
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def game():
    user_cards = []
    user_score = 0
    computer_cards = []
    computer_score = 0
    end = False
    print(logo.logo)
    user_cards.append(random_cards())
    user_cards.append(random_cards())
    computer_cards.append(random_cards())
    computer_cards.append(random_cards())
    print(f"user_cards = {user_cards}")
    print(f"Computer's first card: {computer_cards[0]}")

    while not end:
        if input("Do you wanna another card?: y/n: ") == "y":
            user_cards.append(random_cards())
            user_score = calculation_score(user_cards)
            print(f"user_cards = {user_cards}")
            if user_score > 21:
                end = True
        else:
            user_score = calculation_score(user_cards)
            end = True

    while True:
        if len(computer_cards) < 4 and computer_score < 17:
            computer_cards.append(random_cards())
        computer_score += calculation_score(computer_cards)
        break

    print("==================")

    print(f"User cards = {user_cards}")
    print(f"User score = {user_score}")

    print("==================")

    print(f"computer_cards = {computer_cards}")
    print(f"computer_score = {computer_score}")

    result = compare(user_score, computer_score)
    print(f"RESULT : {result}")


while input("Do you want play again?: y/n: ") == "y":
    replit.clear()
    game()
