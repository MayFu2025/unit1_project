import os
import csv, datetime
from mylib import display_menu, validate_selection, try_login, create_user
startup_menu = ['Already have an account? Log-in', 'New user? Sign-up']
main_menu = ["Create New Transaction", "View Past Transactions", "View Description of DAI Currency", "Log-out"]
ask_return = ["Return to Main Menu", "Save and Log-out"]

# print(logo)
# print("Welcome to your WALLET!") # TODO: Colors! Banners! Yay!
#
# # Log-in or Create User
# print(display_menu(startup_menu))
# selection = validate_selection(startup_menu)
#
# if selection == 1:  # User wants to log-in
#     print('[Log-in to Existing Account]')
#     result = login_function()
#     logged_in = result[0]
#     name = result[1]
#
# if selection == 2:  # User wants to create a new account
#     print('[Create a New Account]')
#     create_user()
#     print("User successfully created. Please log-in.")
#     result = login_function()
#     logged_in = result[0]
#     name = result[1]
#
# # Use a while loop? while logged_in == True (and change logged in to False at end of each selction) and return_to_menu == True:
# # After log-in
# if logged_in == True:
#     print('[Successfully logged in to your wallet.]')
#     print(f"Welcome, {name}!")
#     print(display_menu(main_menu))
#     selection = validate_selection(main_menu)
#     back_to_menu = False
#
# if selection == 1:
#
#     back_to_menu = return_back()
#
# if selection == 2:
#     pass
#
# if selection == 3:
#     pass
#
# if selection == 4:
#     pass
#
# while back_to_menu == True:
#     print(display_menu(main_menu))
#     selection = validate_selection(main_menu)
#     back_to_menu = False

# Log in or Create User
display_menu(startup_menu)
choice = validate_selection(startup_menu)
if choice == 1:
    result = try_login()
    login_success = result[0]
    while login_success == False:
        print("Error: Wrong username or password.")
        result = try_login()
        login_success = result[0]
    user = result[1]
if choice == 2:
    create_user()
    result = try_login()
    login_success = result[0]
    while login_success == False:
        print("Error: Wrong username or password.")
        result = try_login()
        login_success = result[0]
    user = result[1]

# Display main menu and pick function # TODO Can I use a while loop here to repeat the menu after a function should the user specify
if login_success:
    display_menu(main_menu)
    choice = validate_selection(main_menu)
# if choice == 1: # Create new transaction
#     # Thing
# if choice == 2: # View Past Transactions
#     # Thing
# if choice == 3: # View Description of DAI Currency
#     # Thing
if choice == 4: # Log-out
    print("[Logging out...]")
    print("Thank you for using wallet.")
    exit(1)


