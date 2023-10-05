import csv, datetime
from mylib import display_menu, validate_selection, try_login, create_transaction, month_spending, month_statistics, obtain_data, create_bar, logo, ansi, lr, sr, validate_month, validate_year, find_scale

startup_menu = ['Already have an account? Log-in', 'New user? Sign-up']
main_menu = ["Create New Transaction", "View Past Transactions", "View User Statistics", "View Description of DAI Currency", "Log-out"]
ask_return = ["Return to Main Menu", "Save and Log-out"]
transaction_menu = ["Create Deposit", "Create Withdrawal"]
expense_categories = ["Bills", "Necessities", "Transportation", "Subscriptions", "Other"]

# Introduction
print(f"{ansi.get('bold')}{logo}{ansi.get('reset')}")

# Log in or Create User
display_menu(startup_menu)  # startup_menu = ['Already have an account? Log-in', 'New user? Sign-up']
choice = validate_selection(startup_menu)
print(lr)
if choice == 1:
    result = try_login()  # result = [login_success, user]
    login_success = result[0]
    while not login_success:
        print(f"{ansi.get('red')}Error: Wrong username or password.{ansi.get('reset')}")
        result = try_login()
        login_success = result[0]
    user = result[1]
if choice == 2:
    print(f"{ansi.get('bold')}[Create New User]{ansi.get('reset')}")
    with open('users.csv', mode='r') as users_list:
        # Reads the csv file and stores the data in a list
        users_database = users_list.readlines()
    new_name = input("Create an alphanumeric username: ")
    while not new_name.isalnum():
        new_name = input(f"{ansi.get('red')}Error. Please enter a username that is alphanumeric: {ansi.get('reset')}")
    if users_database:  # if users_database is not empty
        validate = True
        while validate:
            for user in users_database:
                if new_name in user:
                    new_name = input(f"{ansi.get('red')}Username already taken. Please enter another username: {ansi.get('reset')}")
                else:
                    validate = False
    new_pass = input("Create an alphanumeric password: ")
    while not new_pass.isalnum():
        new_pass = input(f"{ansi.get('red')}Error. Please enter a password that is alphanumeric: {ansi.get('reset')}")
    confirm_new_pass = input("Confirm new password: ")
    while True:
        if confirm_new_pass != new_pass:
            new_pass = input(f"{ansi.get('red')}Passwords do not match. Create a password: {ansi.get('reset')}")
            confirm_new_pass = input("Confirm new password: ")
        else:
            break
    with open('users.csv', mode='a') as users_list:
        # Adds to the csv file the new user's details
        writer = csv.writer(users_list)
        writer.writerow([new_name, new_pass])
    with open(f"{new_name}.csv", mode='a') as user_data:
        # Creates the csv file for the new user's transaction data
        writer = csv.writer(user_data)
        writer.writerow([datetime.date.today(), 0, "other"])
    print(f"{ansi.get('green')}{ansi.get('bold')}New User Successfully Created. Please log-in.{ansi.get('reset')}")
    print(lr)
    result = try_login()  # result = [login_success, user]
    login_success = result[0]
    while not login_success:
        print(f"{ansi.get('red')}Error: Wrong username or password.{ansi.get('reset')}")
        result = try_login()
        login_success = result[0]
    user = result[1]
print(sr)
print(f"{ansi.get('bold')}{ansi.get('green')}[Successfully Logged-in]{ansi.get('reset')}")

while login_success:
    print(lr)
    print(f"{ansi.get('bold')}[Welcome to your WALLET!]{ansi.get('reset')}")
    display_menu(main_menu)  # main_menu = ["Create New Transaction", "View Past Transactions", "View User Statistics", "View Description of DAI Currency", "Log-out"]
    choice = validate_selection(main_menu)

    if choice == 1:  # Create new transaction
        print(lr)
        print(f"{ansi.get('bold')}[Create New Transaction]{ansi.get('reset')}")
        display_menu(transaction_menu)  # transaction_menu = ["Create Deposit", "Create Withdrawal"]
        choice_a = validate_selection(transaction_menu)
        print(sr)
        create_transaction(select=choice_a, name=user, categories=expense_categories)

    if choice == 2:  # View Past Transactions
        print(lr)
        print(f"{ansi.get('bold')}[View Past Transactions]{ansi.get('reset')}")
        year_selected = input("Choose a year to view data for: ")
        year_selected = validate_year(user=user, year=year_selected)  # ensures that data for the year exists
        month_selected = input("Choose a month to view data for: ")
        month_selected = validate_month(user=user, year=year_selected, month=month_selected)  # ensures that data for the month of that year exists
        data = obtain_data(user)
        print(sr)
        transactions_in_month = f"{ansi.get('bold')}[All Transactions from {year_selected}/{month_selected}]{ansi.get('reset')}\n[Date, Amount, Category]\n"
        for item in data:
            if f"{year_selected}-{int(month_selected):02d}-" in item[0]:
                date = item[0]
                amount = item[1]
                category = item[2]
                transactions_in_month += f"{date}, {amount}, {category}\n"
        print(transactions_in_month)  # prints all transactions in that month

    if choice == 3:  # View User Statistics
        data = obtain_data(name=user)  # data = [[date, amount, category], [date, amount, category], ...]
        total = 0
        profit = 0
        loss = 0
        for item in data:
            transaction = float(item[1])  # transaction = amount
            category = item[2]  # category = category
            if category == "deposit":
                total += transaction
                profit += transaction
            else:
                loss += transaction
                total -= transaction
        if total < 0:
            debt_state = True
        else:
            debt_state = False
        finish = False
        while not finish:
            print(lr)
            print(f"{ansi.get('bold')}[User Statistics: Page 1 of 2]{ansi.get('reset')}\n")
            print(
                f"User was created on: {data[0][0]}\nUser's current balance: {round(total,2)} DAI\nIn debt?: {debt_state}\n")
            print(
                f"Total profit since creation of account: {profit}DAI\nTotal loss since creation of account: {loss}DAI\nProfit to Loss Ratio: {round(profit / loss, 2)}\n")
            # Create Bar Chart for Total Profit/Loss
            print(
                create_bar(title="Chart of Total Profit and Loss", category=["Profit", "Loss"], amounts=[profit, loss],
                           scale=find_scale([profit, loss])))
            print(sr)
            display_menu(["Go to Next Page", "Exit"])
            page = validate_selection([1, 2])
            if page == 2:
                finish = True
            if page == 1:
                print(lr)
                print(f"{ansi.get('bold')}[User Statistics: Page 2 of 2]{ansi.get('reset')}\n")
                validate = True
                year_selected = input("Choose a year to view data for: ")
                year_selected = validate_year(user=user, year=year_selected)  # ensures that data for the year exists
                month_selected = input("Choose a month to view data for: ")
                month_selected = validate_month(user=user, year=year_selected, month=month_selected)  # ensures that data for the month of that year exists
                print(sr)
                month_data = obtain_data(user)  # month_data = [[date, amount, category], [date, amount, category], ...]
                amounts1 = month_statistics(data=month_data, year=int(year_selected), month=int(month_selected))  # amounts1 = [profit, loss]
                amounts2 = month_spending(data=month_data, year=int(year_selected), month=int(month_selected))  # amounts2 = [bills, necessities, transportation, subscriptions, other]
                # Create Bar Charts for Profit/Loss and Expense Categories
                print(create_bar(title=f"Chart of Profit and Loss for {year_selected}/{month_selected}", category=["Profit", "Loss"], amounts=amounts1, scale=find_scale(data= amounts1)))
                print(sr)
                print(create_bar(title=f"Chart of Expense Categories for {year_selected}/{month_selected}", category=expense_categories,
                                 amounts=amounts2, scale=find_scale(data=amounts2)))
                print(sr)
                display_menu(["Go to Previous Page", "Exit"])
                page = validate_selection([1, 2])
            if page == 2:
                finish = True

    if choice == 4:  # View Description of DAI Currency
        print(lr)
        print(f"{ansi.get('bold')}[Description of DAI Currency]{ansi.get('reset')}")
        print("Dai is a token created by MakerDAO, running on the Ethereum blockchain, aims to bring \nstability to the cryptocurrency economy as an unbiased, decentralized stablecoin.\nThe value of 1 Dai token is pegged to approximately 1 USD.\nDai is generated by depositing collateral assets into Maker Vaults in the Maker Protocol.\nThis creates high liquidity and low volatility for Dai.")

    if choice == 5:  # Log-out
        print(lr)
        print(f"{ansi.get('bold')}[Logging out...]{ansi.get('reset')}")
        print("Thank you for using wallet.")
        exit(1)

    print(lr)
    print(f"{ansi.get('bold')}[Return to Main Menu?]{ansi.get('reset')}")
    display_menu(choices=ask_return)  # ask_return = ["Return to Main Menu", "Save and Log-out"]
    log_out = validate_selection([1, 2])
    if log_out == 2:
        print(lr)
        print(f"{ansi.get('bold')}[Logging out...]{ansi.get('reset')}")
        print(f"{ansi.get('italic')}Thank you for using wallet.{ansi.get('reset')}")
        login_success = False