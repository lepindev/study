import art
import alphabet

print(art.logo)


def encrypt(text, key):
    cipher = ""
    for i in text:
        position = alphabet.alphabet.index(i)
        newPosition = position + key
        newLetter = alphabet.alphabet[newPosition]
        cipher += newLetter
    print(cipher)


def decrypt(text, key):
    decrypt = ""
    for i in text:
        position = alphabet.alphabet.index(i)
        newPosition = position - key
        newLetter = alphabet.alphabet[newPosition]
        decrypt += newLetter
    print(decrypt)


userDream = True
while userDream:
    userChoose = input("Hi, enter what you want - encrypt or decrypt: ").lower()
    userText = input("Enter the text: ").lower()
    userKey = int(input("Enter the key: "))
    if userChoose == "encrypt":
        encrypt(userText, userKey)
    if userChoose == "decrypt":
        decrypt(userText, userKey)
    userInput = input("Do you want again? - yes or no: ")
    if userInput == "yes" or userInput == "y":
        print("OKEY, LET'S START")
    elif userInput == "no" or userInput == "n":
        print("OKEY, see ya next time")
        userDream = False
    else:
        print("I don't understand you, BB")
        userDream = False
