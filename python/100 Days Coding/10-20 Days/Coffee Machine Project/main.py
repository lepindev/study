MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 100,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 120,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 130,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def is_sufficient(order):
    for i in order:
        if order[i] > resources[i]:
            print(f"Sorry there is not enough {i}.")
            return False
        return True
def process_coins():
    print("Please enter the coins.")
    total = int(input("How many?"))
    return total

def transaction(money, drink_cost):
    if money > drink_cost:
        change = money - drink_cost
        print(f"There is your change {change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
def make_coffee(order, ingredients):
    for i in ingredients:
        resources[i] -= ingredients[i]
        print(f"Here is your drink {order}")

is_on = True
while is_on:
    choice = input("What would you like to order?: 'espresso' or 'cappuccino' or 'latte': ")
    if choice == "off":
        print("The coffee machine is turning off")
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk {resources['milk']}ml")
        print(f"coffee {resources['coffee']}g")
        print(f"Money {profit}")
    else:
        drink = MENU[choice]
        if is_sufficient(drink["ingredients"]):
            payment = process_coins()
            if transaction(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
