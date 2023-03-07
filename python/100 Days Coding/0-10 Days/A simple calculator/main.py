import art
import operations_function
import replit

print(art.logo)

operations = {
    "+": operations_function.add,
    "-": operations_function.subtract,
    "*": operations_function.multiply,
    "/": operations_function.division,
}

number1 = float(input("What's the first number?: "))


while True:
    for i in operations:
        print(i)
    user_choise = input("What's the operation?: ")
    number2 = float(input("What's the next number?: "))
    calculation = operations[user_choise]
    answer = calculation(number1, number2)
    print(f"{number1} {user_choise} {number2} = {answer}")
    if input("Continue calculation or reset? y/N: ") == "y":
        number1 = answer
    else:
        print("Bye")
        break
    replit.clear()
    print(number1)
