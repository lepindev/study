import art
import replit
print(art.logo)

print("Welcome to the secren auction program.")

end = False
result = {}


def findWinner(result):
    maximum = 0
    winner = ""
    for key in result:
        value = result[key]
        if value > maximum:
            maximum = value
            winner = key
    print(f"The winner is {winner} with a bid of {maximum}")



while not end:
    name = input("What's your name?")
    bid = int(input("What's your bid?: $"))
    result[name] = bid
    shouldContinue = input("Are there any other bidders? Type 'yes' or 'no':" )
    if shouldContinue == "yes" or shouldContinue == 'y':
        replit.clear()
    else:
        end = True
        replit.clear()
        findWinner(result)
