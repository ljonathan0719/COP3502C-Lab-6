# Jonathan Li
menu_selection = ""

# encoder Function
def encoder(password):
    encoded_pass = ""
    for i in password:
        value = int(i) - 3
        if value < 0:  # cannot have value greater than 9 in any password
            value += 10
        encoded_pass += str(value)
    return encoded_pass

# menu function
def menu():
    print("Menu")
    print("-------------")
    print("1. Encode\n2. Decode\n3. Quit")
    menu_selection = input("Please enter an option: ")

    return menu_selection

#decoder function
def decoder(encoded_pass):
    decoded_pass = ''
    for num in encoded_pass:
        value = int(num) + 3
        if value >= 10:  # cannot have value greater than 9 in any password
            value -= 10
        decoded_pass += str(value)

    return decoded_pass


# global function
if __name__ == "__main__":
    menu_selection = menu()
    while menu_selection != 3:
        menu()
        menu_selection = input("Please enter an option: ")
        if menu_selection == 1:
            password = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")
        if menu_selection == 2:
            encoded_pass = input("Please enter your encoded password: ")
            decoded_pass = decoder(encoded_pass)
            print(f"The encoded password is {encoded_pass}, and the original password is {decoded_pass}. ")
