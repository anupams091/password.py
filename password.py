def generator():
    import random
    length = int(input("The recommended length is atleast 8, how long should your password be: "))
    list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y',
            'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$',
            '^', '%',
            '&', '*', '(', ')', '_', '+']
    password = ''
    for i in range(1, length):
        password += random.choice(list)
    print(password)
    toStrength = input("Would you like to check the strength of this password?(Y/N): ")
    if toStrength == 'Y':
        strengthChecker()
    else:
        quit()
def strengthChecker():
    a,b,c,d = 0,0,0,0
    password = input("Enter your password: ")
    capletters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowerletters = 'abcdefghijklmnopqrstuvwxyz'
    numbers = '1234567890'
    specialCharacters = '!@#$%^&*()_-+'
    if len(password) >= 8: #This if statement checks for the length to make sure it is atleast 10 characters
        for i in password: #The for loops basically runs a tally on the type of characters present in the password
            if (i in capletters):
                a+=1
            if (i in lowerletters):
                b+=1
            if (i in numbers):
                c+=1
            if (i in specialCharacters):
                d+=1
        if (a >= 1, b >= 1, c >= 1, d >= 1): #This if checks if each type is present atleast once
                print("valid password!")
    else:
        WeakPass = input("Weak password! Enter '3' to try another password or '4' to use our password generator or '0' to exit: ")
        if WeakPass == '3':
            strengthChecker()
        elif WeakPass == '4':
            generator()
        else:
            quit()
def mainFunction():
    choice = input("What would you like to do? (Enter '1' to generate a password, Enter '2' to check the strength or Enter '0' anytime to cancel: ")
    if choice == '1':
        generator()
    elif choice == '2':
        strengthChecker()
    elif choice == '0':
        quit()
    else:
        print("Invalid response!")
        while choice != '1' and '2':
            mainFunction()
mainFunction()


