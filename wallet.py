import os
import csv, datetime
from stylize import logo, ascii_colors, hr
from mylib import display_menu, validate_selection, try_login, create_user, create_transaction, month_spending, month_statistics, obtain_data, create_bar

startup_menu = ['Already have an account? Log-in', 'New user? Sign-up']
main_menu = ["Create New Transaction", "View Past Transactions", "View Description of DAI Currency", "Log-out"]
ask_return = ["Return to Main Menu", "Save and Log-out"]
transaction_menu = ["Create Deposit", "Create Withdrawal"]
expense_categories = ["Bills", "Necessities", "Transportation", "Subscriptions", "Other"]

# TODO: Colors! Banners! Yay!
# TODO: Add spaces between lines

# Introduction
print(logo)

# Log in or Create User
display_menu(startup_menu)
choice = validate_selection(startup_menu)
print(hr)
if choice == 1:
    print("[Log-in]")
    result = try_login()
    login_success = result[0]
    while not login_success:
        print("Error: Wrong username or password.")
        result = try_login()
        login_success = result[0]
    user = result[1]
if choice == 2:
    print("[Create New User]")
    create_user()
    print("New User Successfully Created. Please log-in.")
    # TODO: You can supposedly create a user with the name ' ' and password ' ' and it will still work. You can't log into it though. Better to make it so that you can't create a user with a space in the name or password.
    # TODO: Should probably make usernames only alphanumeric, and passwords only alphanumeric and symbols.
    result = try_login()
    login_success = result[0]
    while not login_success:
        print("Error: Wrong username or password.")
        result = try_login()
        login_success = result[0]
    user = result[1]

while login_success:
    print(hr)
    print("[Successfully Logged-in]")
    print("Welcome to your WALLET!")
    display_menu(main_menu)
    choice = validate_selection(main_menu)

    if choice == 1:  # Create new transaction
        print(hr)
        print("[Create New Transaction]")
        display_menu(transaction_menu)
        choice_a = validate_selection(transaction_menu)
        # TODO: I kinda want like only one empty line here but hr gives me this huge ass space lol
        # TODO: I got up to here for creating spacing yay
        create_transaction(select=choice_a, name=user, expense_categories=expense_categories)

    if choice == 2:  # View Past Transactions
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
        page_2 = (
            f"Total profit since creation of account: {profit}DAI\nTotal loss since creation of account: {loss}DAI\n")
        finish = False
        while not finish:
            print(f"[User Statistics]\n[Page 1 of 2]")
            print(
                f"User was created on: {data[0].split(',')[0]}\nUser's current balance: {total} DAI\nIn debt?: {debt_state}\n")
            print(
                f"Total profit since creation of account: {profit}DAI\nTotal loss since creation of account: {loss}DAI\nProfit to Loss Ratio: {round(profit / loss, 2)}")
            print(
                create_bar(title="Chart of Total Profit and Loss", category=["Profit", "Loss"], amounts=[profit, loss],
                           scale=100))
            display_menu(["Go to Next Page", "Exit"])
            page = validate_selection([1, 2])
            if page == 2:
                finish = True
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
                print(create_bar(title="Chart of Profit and Loss for Selected Month", category=["Profit", "Loss"],
                                 amounts=month_statistics(data=obtain_data(user), year=2023, month=month_selected),
                                 scale=100))
                print(create_bar(title="Chart of Expense Categories for Selected Month", category=expense_categories,
                                 amounts=month_spending(data=obtain_data(user), year=2023, month=month_selected),
                                 scale=10))
                display_menu(["Go to Previous Page", "Exit"])
                page = validate_selection([1, 2])
            if page == 2:
                finish = True

    if choice == 3:  # View Description of DAI Currency #TODO: Make this look better lmao
        print(
            "Dai is a token created by MakerDAO, running on the Ethereum blockchain, aims to bring stability to the cryptocurrency economy as an unbiased, decentralized stablecoin. The value of 1 Dai token is pegged to approximately 1 USD. Dai is generated by depositing collateral assets into Maker Vaults in the Maker Protocol. This creates high liquidity and low volatility for Dai.")

    if choice == 4:  # Log-out
        print("[Logging out...]")
        print("Thank you for using wallet.")
        exit(1)

    print("[Return to Main Menu?]]")
    display_menu(choices=ask_return)
    log_out = validate_selection([1, 2])
    if log_out == 2:
        print("[Logging out...]")
        print("Thank you for using wallet.")
        login_success = False