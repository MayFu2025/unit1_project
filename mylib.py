import csv, datetime
def display_menu(choices: list):
    '''Takes a list and prints a menu with each item of the list being a choice in the menu.'''
    menu = ''
    count = 1
    for it in choices:
        menu += f"{it.ljust(50, '.')} type {count}\n"
        count += 1
    print(menu)

def validate_selection(choices: list) -> int:
    '''Takes a list and a int user input, checks if the user input is within the number of choices available in the menu. Returns the int selection.'''
    expect = len(choices)
    select = input(f'Select a choice between 1~{expect}: ')
    while not 0 < int(select) < expect+1: # TODO: Error when string inputted instead
        select = input(f"Error. Please select a choice between 1~{expect}: ")
    select = int(select)
    return select

def try_login() -> tuple:
    '''Tests if user can successfully log in. Returns a tuple on bool: success of log-in, and str: user of current session.'''
    with open('users.csv', mode='r') as f:
        data = f.readlines()
    success = False

    in_name = input("Enter your username: ")
    in_pass = input("Enter your password: ")

    for line in data:
        uname = line.split(',')[0]
        upass = line.split(',')[1].strip()  # strip() removes \n for any string unless specified

        if uname == in_name and upass == in_pass:
            success = True
            break

    return success, uname

def create_user():
    '''Creates a new user and adds them to users.csv. Takes user input new_name and new_pass.'''
    with open('users.csv', mode='r') as users_list:
        users_database = users_list.readlines()
    new_name = input("Create a username: ")
    if users_database:
        validate = True
        while validate == True:
            for user in users_database:
                if new_name in user:
                    new_name = input("Username already taken. Please enter another username: ")
                else:
                    validate = False
    new_pass = input("Create a password: ")
    confirm_new_pass = input("Confirm new password: ")
    validate = True
    while validate == True:
        if confirm_new_pass != new_pass:
            new_pass = input("Passwords do not match. Create a password: ")
            confirm_new_pass = input("Confirm new password: ")
        else:
            validate = False
    with open('users.csv', mode='a') as users_list:
        writer = csv.writer(users_list)
        writer.writerow([new_name, new_pass])
    with open(f"{new_name}.csv", mode='a') as user_data:
        writer = csv.writer(user_data)
        writer.writerow([datetime.date.today(), 0])

expense_categories = ["Bills", "Necessities", "Transportation", "Subscriptions", "Other"]
def create_transaction(select: int, name: str, expense_categories: list):
    action_date = datetime.date.today()
    if select == 1:  # User Create Transaction
        raw_dep = input("Enter amount of DAI you would like to deposit: ")
        while not raw_dep.isdigit():
            raw_dep = input("Error. Please enter as a numeric value how much DAI you would like to deposit: ")
        action_value = float(raw_dep)
        with open(f"{name}.csv", 'a') as user_data:
            user_data.writelines(f"{action_date},{action_value},deposit\n")
    if select == 2:
        raw_wtd = input("Enter amount of DAI you would like to withdraw: ")
        while not raw_wtd.isdigit():
            raw_wtd = input("Error. Please enter as a numeric value how much DAI you would like to withdraw: ")
        action_value = -(float(raw_wtd))
        display_menu(expense_categories)
        category = validate_selection(expense_categories)
        if category == 1:
            category = "bills"
        elif category == 2:
            category = "necessities"
        elif category == 3:
            category = "transportation"
        elif category == 4:
            category = "subscriptions"
        elif category == 5:
            category = "other"
        with open(f"{name}.csv", 'a') as user_data:
            user_data.writelines(f"{action_date},{action_value},{category}\n")


# page_1 = f"""
# User was created on: {data[0].split(',')[0]}
# User's current balance: {total} DAI
# In debt?: {debt_state}
# Total amount deposited: {}DAI
# Total amount withdrawn: {}DAI"""
#
# page_2 = f"""
#
# """

def obtain_data(name: str, start_date: str, end_date: str):
    with open(f'{name}.csv', mode='r') as user_list:
        transaction_database = user_list.readlines()
    dates = []
    reversed = []
    transaction = []
    for item in transaction_database:
        data = item.strip().split(',')
        date = data[0]
        dates.append(date)
        reversed.append(date)
        category = data[2]
        amount = data[1]
        transaction.append([category,amount])
    reversed.reverse()
    iStart = dates.index(start_date)
    iEnd = -(reversed.index(end_date))-1
    profit = 0
    loss = 0
    for i in range(iStart, iEnd-1):
        print(transaction[i][1])
        print(transaction[i][1])
        if transaction[i][0] == 'deposit':
            profit += transaction[i][1]
        else:
            loss += transaction[i][1]
    print(profit)
    print(loss)

obtain_data('test', '2023-09-24', '2023-09-26')


# def past_month():
#

# with open(f'test.csv', mode='r') as user_list:
#     transaction_database = user_list.readlines()
# print(transaction_database)
# create_graph(name="test", start_date='2023-09-24', end_date='2023-09-26')
# dates = []
# for item in transaction_database:
#     date = item.strip()
#     date = date.split(',')[0]
#     dates.append(date)
# iStart = dates.index('start_date')
