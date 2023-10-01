import csv, datetime, maskpass


def display_menu(choices: list):
    '''Takes a list and prints a menu with each item of the list being a choice in the menu.'''
    menu = ''
    count = 1
    for it in choices:
        menu += f"{it.ljust(50, '.')} type {count}\n"
        count += 1
    print(menu)


def validate_selection(choices: list) -> int:
    '''Takes a list and an int user input, checks if the user input is within the number of choices available in the menu. Returns the int selection.'''
    expect = len(choices)
    select = input(f'Select a choice between 1~{expect}: ')
    while not select.isnumeric():
        select = input(f"Error. Please select a choice between 1~{expect}: ")
    while True:
        if not select.isnumeric() or not 0 < int(select) < expect + 1:
            select = input(f"Error. Please select a choice between 1~{expect}: ")
        else:
            break
    select = int(select)
    return select

def validate_year(user: str, year: str)-> str:
    data = obtain_data(user)
    earliest_year = data[0][0].split('-')[0]
    latest_year = data[-1][0].split('-')[0]
    while True:
        if year.isnumeric() and int(earliest_year) <= int(year) <= int(latest_year):
            break
        else:
            print("Error. The year selected you selected has no data, or you have entered a non-numeric value.")
            year = input(f"Choose a year to view data for: ")
    return year

def validate_month(user: str, month: str, year: str) -> str:
    data = obtain_data(user)
    data_exists = False
    while not data_exists:
        if not month.isnumeric():
            print("Error. You have entered a non-numeric value.")
            month = input("Choose a month to view data for: ")
            pass
        else:
            for item in data:
                if f"{year}-" in item[0]:
                    if f"-{int(month):02d}-" in item[0]:
                        data_exists = True
                        break
        if data_exists:
            return month
    else:
        print("Error. The month you selected has no data.")
        month = input("Choose a month to view data for: ")

# def validate_selection(choices: list)-> int:
#     '''Takes a list and a int user input, checks if the user input is within the number of choices available in the menu. Returns the int selection.'''
#     expect = len(choices)
#     select = input(f'Select a choice between 1~{expect}: ')
#     while not select.isnumeric():
#         select = input(f"Error. Please select a choice between 1~{expect}: ")
#         try:
#             select = int(select)
#         except ValueError:
#             select = input(f"Error. Please select a choice between 1~{expect}: ")
#     while not 0 < int(select) < expect+1:
#         select = input(f"Error. Please select a choice between 1~{expect}: ")
#         return int(select)

def validate_float(user_input: str) -> bool:
    '''Takes a str user input and checks if it is a float. Returns a boolean.'''
    try:
        float(user_input)
        return True
    except ValueError:
        return False


def try_login() -> tuple:
    '''Tests if user can successfully log in. Returns a tuple on bool: success of log-in, and str: user of current session.'''
    print("[Log-in]")
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
    print("[Create New User]")
    with open('users.csv', mode='r') as users_list:
        users_database = users_list.readlines()
    new_name = input("Create an alphanumeric username: ")
    while not new_name.isalnum():
        new_name = input("Error. Please enter a username that is alphanumeric: ")
    if users_database:  # if users_database is not empty
        validate = True
        while validate:
            for user in users_database:
                if new_name in user:
                    new_name = input("Username already taken. Please enter another username: ")
                else:
                    validate = False
    new_pass = input("Create an alphanumeric password: ")
    while not new_pass.isalnum():
        new_pass = input("Error. Please enter a password that is alphanumeric: ")
    confirm_new_pass = input("Confirm new password: ")
    while True:
        if confirm_new_pass != new_pass:
            new_pass = input("Passwords do not match. Create a password: ")
            confirm_new_pass = input("Confirm new password: ")
        else:
            break
    with open('users.csv', mode='a') as users_list:
        writer = csv.writer(users_list)
        writer.writerow([new_name, new_pass])
    with open(f"{new_name}.csv", mode='a') as user_data:
        writer = csv.writer(user_data)
        writer.writerow([datetime.date.today(), 0, "other"])


def create_transaction(select: int, name: str, categories: list):
    '''Creates a transaction for the user. Takes user input select, name, and expense_categories.'''
    action_date = datetime.date.today()
    if select == 1:  # User Create Transaction
        print("[New Deposit]")
        raw_dep = input("Enter amount of DAI you would like to deposit: ")
        while not validate_float(raw_dep):
            raw_dep = input("Error. Please enter how much DAI you would like to deposit: ")
        action_value = float(raw_dep)
        category = "deposit"
    if select == 2:
        print("[New Withdrawal]")
        raw_wtd = input("Enter amount of DAI you would like to withdraw: ")
        while not validate_float(raw_wtd):
            raw_dep = input("Error. Please enter how much DAI you would like to deposit: ")
        action_value = -(float(raw_wtd))
        print(sr)
        print("Select a Category for your Withdrawal:")
        display_menu(categories)
        category = categories[validate_selection(categories)-1].lower()

    with open(f"{name}.csv", 'a') as user_data:
        user_data.writelines(f"{action_date},{action_value},{category}\n")
    print(f"Transaction Recorded: On {action_date}, {action_value} DAI as {category} on {name}'s wallet.")


def obtain_data1(name: str, start_date: str, end_date: str):
    """My attempt at obtaining data in a csv file between a specified start date and specified end date. Chotto not working so it's unused. Obtains data from a csv file and returns a list of lists with each list containing the date, amount, and category of a transaction."""
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
        transaction.append([category, amount])
    reversed.reverse()
    iStart = dates.index(start_date)
    iEnd = -(reversed.index(end_date)) - 1
    profit = 0
    loss = 0
    for i in range(iStart, iEnd - 1):  # the for loop itself isn't working
        if transaction[i][0] == 'deposit':
            profit += transaction[i][1]
        else:
            loss += transaction[i][1]


obtain_data1('test', '2023-09-24', '2023-09-26')


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

def obtain_data(name: str) -> list:
    """Obtains data from a csv file and returns a list of lists with each list containing the date, amount, and category of a transaction."""
    with open(f'{name}.csv', mode='r') as user_list:
        transaction_database = user_list.readlines()
    data = []
    for item in transaction_database:
        date, amount, category = item.strip().split(",")
        data.append([date, amount, category])
    return data


def month_statistics(data: list, month: int, year: int):  # to validate month, use a list with numbers from 1 to 12
    """Find the total profit and loss in a specified month of a specified year."""
    profit = 0
    loss = 0
    for item in data:
        if f"{year}-{month:02d}-" in str(item[0]):
            if item[2] == 'deposit':
                profit += float(item[1])
            else:
                loss += -(float(item[1]))
    return [profit, loss]


def month_spending(data: list, month: int, year: int) -> list:
    """Find the total spending in each category in a specified month of a specified year."""
    bills = 0
    necessities = 0
    transportation = 0
    subscriptions = 0
    other = 0
    for item in data:
        if f"{year}-{month:02d}-" in str(item[0]):
            if item[2] == 'bills':
                bills += float(item[1])
            elif item[2] == 'necessities':
                necessities += float(item[1])
            elif item[2] == 'transportation':
                transportation += float(item[1])
            elif item[2] == 'subscriptions':
                subscriptions += float(item[1])
            elif item[2] == 'other':
                other += float(item[1])
    return [bills, necessities, transportation, subscriptions, other]


# TODO: Find a suitable scale function?
def create_bar(title: str, category: list, amounts: list, scale: int) -> str:
    """Creates a bar chart with a title, categories, amounts, and a scale."""
    bar_chart = f"{title}\n"
    for i in range(
            len(category)):  # TODO: the round function only rounds to nearest whole, is it possible to round to nearest multiple of scale?
        amount_bar = abs(amounts[i]) // scale
        bar_category = f"{category[i].ljust(20)}"
        for x in range(int(amount_bar)):
            bar_category += '▥'
        bar_chart += f"{bar_category} {abs(amounts[i])} DAI\n"
    bar_chart += f"Where each ▥ represents {scale} DAI"
    return bar_chart


# Stylization Tools #
logo = """
 __     __     ______     __         __         ______     ______  
/\ \  _ \ \   /\  __ \   /\ \       /\ \       /\  ___\   /\__  _\ 
\ \ \/ ".\ \  \ \  __ \  \ \ \____  \ \ \____  \ \  __\   \/_/\ \/ 
 \ \__/".~\_\  \ \_\ \_\  \ \_____\  \ \_____\  \ \_____\    \ \_\ 
  \/_/   \/_/   \/_/\/_/   \/_____/   \/_____/   \/_____/     \/_/ 

"""

ascii_colors = {
    "reset": "\033[0m",
    "bold": "\033[1m",
    "dim": "\033[2m",
    "italic": "\033[3m",
    "underline": "\033[4m",
    "blink": "\033[5m",
    "reverse": "\033[7m",
    "hidden": "\033[8m",

    "black": "\033[30m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",

    "bg_black": "\033[40m",
    "bg_red": "\033[41m",
    "bg_green": "\033[42m",
    "bg_yellow": "\033[43m",
    "bg_blue": "\033[44m",
    "bg_magenta": "\033[45m",
    "bg_cyan": "\033[46m",
    "bg_white": "\033[47m"
}

lr = "\n"
sr = ""