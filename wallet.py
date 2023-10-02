from mylib import display_menu, validate_selection, try_login, create_user, create_transaction, month_spending, month_statistics, obtain_data, create_bar, logo, ascii_colors, lr, sr, validate_month, validate_year, find_scale

startup_menu = ['Already have an account? Log-in', 'New user? Sign-up']
main_menu = ["Create New Transaction", "View Past Transactions", "View User Statistics", "View Description of DAI Currency", "Log-out"]
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
print(lr)
if choice == 1:
    result = try_login()
    login_success = result[0]
    while not login_success:
        print("Error: Wrong username or password.")
        result = try_login()
        login_success = result[0]
    user = result[1]
if choice == 2:
    create_user()
    print("New User Successfully Created. Please log-in.")
    print(lr)
    result = try_login()
    login_success = result[0]
    while not login_success:
        print("Error: Wrong username or password.")
        result = try_login()
        login_success = result[0]
    user = result[1]
print(sr)
print("[Successfully Logged-in]")

while login_success:
    print(lr)
    print("[Welcome to your WALLET!]")
    display_menu(main_menu)
    choice = validate_selection(main_menu)

    if choice == 1:  # Create new transaction
        print(lr)
        print("[Create New Transaction]")
        display_menu(transaction_menu)
        choice_a = validate_selection(transaction_menu)
        print(sr)
        create_transaction(select=choice_a, name=user, categories=expense_categories)

    if choice == 2:  # View Past Transactions
        print(lr)
        print("[View Past Transactions]")
        year_selected = input("Choose a year to view data for: ")
        year_selected = validate_year(user=user, year=year_selected)
        month_selected = input("Choose a month to view data for: ")
        print(sr)
        month_selected = validate_month(user=user, year=year_selected, month=month_selected)
        data = obtain_data(user)
        transactions_in_month = f"[All Transactions from {year_selected}/{month_selected}]\n"
        for item in data: #TODO looks bad cause of list format
            if f"{year_selected}-{int(month_selected):02d}-" in str(item[0]):
                transactions_in_month += f"{item}\n"
        print(transactions_in_month)


    if choice == 3:  # View User Statistics
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
        finish = False
        while not finish:
            print(lr)
            print(f"[User Statistics: Page 1 of 2]\n")
            print(
                f"User was created on: {data[0].split(',')[0]}\nUser's current balance: {total} DAI\nIn debt?: {debt_state}\n")
            print(
                f"Total profit since creation of account: {profit}DAI\nTotal loss since creation of account: {-loss}DAI\nProfit to Loss Ratio: {round(profit / -loss, 2)}\n")
            print(
                create_bar(title="Chart of Total Profit and Loss", category=["Profit", "Loss"], amounts=[profit, loss],
                           scale=find_scale([profit, -loss])))
            print(sr)
            display_menu(["Go to Next Page", "Exit"])
            page = validate_selection([1, 2])
            if page == 2:
                finish = True
            if page == 1:
                print(lr)
                print(f"[User Statistics: Page 2 of 2]\n")
                validate = True
                year_selected = input("Choose a year to view data for: ")
                year_selected = validate_year(user=user, year=year_selected)
                month_selected = input("Choose a month to view data for: ")
                month_selected = validate_month(user=user, year=year_selected, month=month_selected)
                print(sr)
                month_data = obtain_data(user)
                amounts1 = month_statistics(data=month_data, year=int(year_selected), month=int(month_selected))
                amounts2 = month_spending(data=month_data, year=int(year_selected), month=int(month_selected))
                print(create_bar(title=f"Chart of Profit and Loss for {year_selected}/{month_selected}", category=["Profit", "Loss"], amounts=amounts1, scale=find_scale(data= amounts1)))
                print(sr)
                print(create_bar(title=f"Chart of Expense Categories for {year_selected}/{month_selected}", category=expense_categories,
                                 amounts=amounts2, scale=find_scale(data=amounts2)))
                print(sr)
                display_menu(["Go to Previous Page", "Exit"])
                page = validate_selection([1, 2])
            if page == 2:
                finish = True

    if choice == 4:  # View Description of DAI Currency #TODO: Make this look better lmao
        print(lr)
        print("[Description of DAI Currency]")
        print("Dai is a token created by MakerDAO, running on the Ethereum blockchain, aims to bring \nstability to the cryptocurrency economy as an unbiased, decentralized stablecoin.\nThe value of 1 Dai token is pegged to approximately 1 USD.\nDai is generated by depositing collateral assets into Maker Vaults in the Maker Protocol.\nThis creates high liquidity and low volatility for Dai.")

    if choice == 5:  # Log-out
        print(lr)
        print("[Logging out...]")
        print("Thank you for using wallet.")
        exit(1)

    print(lr)
    print("[Return to Main Menu?]")
    display_menu(choices=ask_return)
    log_out = validate_selection([1, 2])
    if log_out == 2:
        print(lr)
        print("[Logging out...]")
        print("Thank you for using wallet.")
        login_success = False