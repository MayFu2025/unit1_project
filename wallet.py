import os
import csv, datetime
from mylib import display_menu, validate_selection, try_login, create_user, create_transaction, month_spending, month_statistics, obtain_data, create_bar
startup_menu = ['Already have an account? Log-in', 'New user? Sign-up']
main_menu = ["Create New Transaction", "View Past Transactions", "View Description of DAI Currency", "Log-out"]
ask_return = ["Return to Main Menu", "Save and Log-out"]
transaction_menu = ["Create Deposit", "Create Withdrawal"]
expense_categories = ["Bills", "Necessities", "Transportation", "Subscriptions", "Other"]

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
    print("New User Successfully Created. Please log-in.")
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

if choice == 1: # Create new transaction
    display_menu(transaction_menu)
    choice_a = validate_selection(transaction_menu)
    create_transaction(select=choice_a, name=user, expense_categories=expense_categories)

if choice == 2: # View Past Transactions
    with open(f'{user}.csv', mode='r') as f:
        data = f.readlines()
    total = 0
    profit = 0
    loss = 0
    for line in data:
        transaction = float(line.split(',')[1])
        total += transaction
        if transaction < 0:
            loss += transaction
        elif transaction > 0:
            profit += transaction
    if total < 0:
        debt_state = True
    else:
        debt_state = False
    page_2 = (f"Total profit since creation of account: {profit}DAI\nTotal loss since creation of account: {loss}DAI\n")
    exit = False
    while not exit: #TODO: exit variable to decide whether user has chosen to exit or see next page
        print(f"[User Statistics]\n[Page 1 of 2]")
        print(f"User was created on: {data[0].split(',')[0]}\nUser's current balance: {total} DAI\nIn debt?: {debt_state}\n")
        print(f"Total profit since creation of account: {profit}DAI\nTotal loss since creation of account: {loss}DAI\nProfit to Loss Ratio: {round(profit / loss, 2)}")
        print(create_bar(title="Chart of Total Profit and Loss", category=["Profit", "Loss"], amounts=[profit, loss], scale=100))
        display_menu(["Go to Next Page", "Exit"])
        page = validate_selection([1,2]) #Selecting two takes you to page 2 instead of exit
        if page == 2:
            exit = True
        if page == 1:
            print(f"[User Statistics]\n[Page 2 of 2]")
            validate = True
            year_selected = input("Choose a year to view data for: ")
            while validate:
                if year_selected.isnumeric():
                    year_selected = int(year_selected)
                    validate = False
                else:
                    year_selected = input("Error. Please choose a year to view data for: ")
            print("Choose a month to view data for: ")
            month_selected = validate_selection([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
            print(create_bar(title="Chart of Profit and Loss for Selected Month", category=["Profit", "Loss"], amounts=month_statistics(data=obtain_data(user), year=2023, month=month_selected), scale=100))
            print(create_bar(title="Chart of Expense Categories for Selected Month", category=expense_categories, amounts=month_spending(data=obtain_data(user), year=2023, month=month_selected), scale=10))
            display_menu(["Go to Previous Page", "Exit"])
            page = validate_selection([1, 2])
        if page == 2:
            exit = True


if choice == 3: # View Description of DAI Currency #TODO: Make this look better lmao
    print("Dai is a token created by MakerDAO, running on the Ethereum blockchain, aims to bring stability to the cryptocurrency economy as an unbiased, decentralized stablecoin. The value of 1 Dai token is pegged to approximately 1 USD. Dai is generated by depositing collateral assets into Maker Vaults in the Maker Protocol. This creates high liquidity and low volatility for Dai.")

if choice == 4: # Log-out
    print("[Logging out...]")
    print("Thank you for using wallet.")
    exit(1)


