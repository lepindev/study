import random
import string

letters = string.ascii_letters
digits = string.digits
characters = letters + digits

lettersInput = int(
    input("Hello, Welcome to the Password-Generator\nHow many symbols would you like?")
)
password = []
for i in range(0, lettersInput, 1):
    password.append(random.choice(characters))
password = "".join(password)
print(f"Here is your password: {password}")
