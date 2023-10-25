# Jonathan Li
menu_selection = ""

def encoder(password):
    encoded_pass = ""
    for i in password:
        value = int(i) + 3
        if value >= 10:
            value -= 10
        encoded_pass += str(value)
    return encoded_pass

def menu():
    print("Menu")
    print("-------------")
    print("1. Encode\n2. Decode\n3. Quit")


if __name__ == "__main__":
    while menu_selection != 3:
        menu()
        menu_selection = input("Please enter an option: ")
        if menu_selection == 1:
            password = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")
        if menu_selection == 2:
            decoder(encoded_password)
            print(f"The encoded password is {encoded_pass}, and the original password is {decoded_pass}. ")
