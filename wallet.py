from login import create_user, login_success, try_login, login_function
from menu import display_menu, validate_selection, logo
startup = ['Already have an account? Log-in', 'New user? Sign-up']
main_menu = ["Create New Transaction", "View Past Transactions", "View Description of DAI Currency", "Log-out"]
ask_return = ["Return to Main Menu", "Save and Log-out"]


def return_back():
    display_menu(ask_return)
    choice = validate_selection(ask_return)
    if choice == 1:
        return True
    if choice == 2:
        return False
back_to_menu = False

print(logo)
print("Welcome to your WALLET!") # TODO: Colors! Banners! Yay!

# Log-in or Create User
print(display_menu(startup))
selection = validate_selection(startup)

if selection == 1:  # User wants to log-in
    print('[Log-in to Existing Account]')
    result = login_function()
    logged_in = result[0]
    name = result[1]

if selection == 2:  # User wants to create a new account
    print('[Create a New Account]')
    create_user()
    print("User successfully created. Please log-in.")
    result = login_function()
    logged_in = result[0]
    name = result[1]

# Use a while loop? while logged_in == True (and change logged in to False at end of each selction) and return_to_menu == True:
# After log-in
if logged_in == True:
    print('[Successfully logged in to your wallet.]')
    print(f"Welcome, {name}!")
    print(display_menu(main_menu))
    selection = validate_selection(main_menu)
    back_to_menu = False

if selection == 1:
    back_to_menu = return_back()

if selection == 2:
    pass

if selection == 3:
    pass

if selection == 4:
    pass

while back_to_menu == True:
    print(display_menu(main_menu))
    selection = validate_selection(main_menu)
    back_to_menu = False