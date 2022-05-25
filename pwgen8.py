import random

def generatePassword():
    print("Welcome to Password Generator!")

    char = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"

    while 1:
        passwordLength = input("Please enter desired password length between 8 to 20: ")
        if passwordLength.isnumeric():
            passwordLength = int(passwordLength)
            if passwordLength < 8 or passwordLength > 20:
                print("invalid password length!")
                continue
            print("Generated password:")
            for i in range(0, passwordLength):
                print(char[random.randrange(len(char))], end="")
            print()
        else:
            print("invalid password length!")

generatePassword()

    