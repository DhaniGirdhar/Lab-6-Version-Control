# function to encode passkey, where each digit is shifted right 3 (3 is added to the value of each digit)
def encode(passkey):
    encoded_passkey = ""
    for digit in passkey:
        encoded_passkey += str((int(digit) + 3) %10)
    return encoded_passkey

# function to call menu, without taking up space in main
def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()

if __name__ == '__main__':

    # option is not from the menu (since those would prompt further code) and is less than 3
    option = 0

    #while option is either options 1 or 2 and not 3 (exit) or greater (invalid), loop code
    while option < 3:

        menu()

        option = int(input("Please enter an option: "))

        # encode inputted password
        if option == 1:
            password = input("Please enter your password to encode: ")
            encoded = encode(password)
            print("Your password has been encoded and stored!")
            print()

        # display encoded password, along with original inputted password
        if option == 2:
            # to implement

        # quit
        if option == 3:
            break
