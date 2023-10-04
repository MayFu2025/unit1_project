import csv, datetime, maskpass


def display_menu(choices: list):
    """Displays a menu with choices from a list.
    :param choices: list containing strings of choices in a menu
    """

    menu = ''
    count = 1
    for it in choices:
        menu += f"{it.ljust(50, '.')} type {count}\n"
        count += 1
    print(menu)


def validate_selection(choices: list) -> int:
    """Takes a list and a int user input, checks if the user input is within the number of choices available in the menu. Returns the int selection.
    :param choices: list
        A list containing strings of choices in a menu
    :return: int
        The final selection of user as an integer corresponding to the choices in list
    """

    expect = len(choices)
    select = input(f'Select a choice between 1~{expect}: ')
    while True:
        if not select.isnumeric() or not 0 < int(select) < expect + 1:
            select = input(f"{ansi.get('red')}Error. Please select a choice between 1~{expect}: {ansi.get('reset')}")
        else:
            break
    select = int(select)
    return select

def validate_year(user: str, year: str)-> str:
    """Takes a str user input and checks if it is a valid year, and if the user's account exists in that year. Returns a str year.
    :param user: str
        The username of user of the current session
    :param year: str
        The year selected by user
    :return year: str
        The final year selected by user after validation
    """
    data = obtain_data(user)
    earliest_year = data[0][0].split('-')[0]
    latest_year = data[-1][0].split('-')[0]
    while True:
        if year.isnumeric() and int(earliest_year) <= int(year) <= int(latest_year):
            break
        else:
            print(f"{ansi.get('red')}Error. The year selected you selected has no data, or you have entered a non-numeric value.{ansi.get('reset')}")
            year = input(f"Choose a year to view data for: ")
    return year


def validate_month(user: str, year: str, month: str) -> str:
    """Takes a str user input and checks if it is a valid month, and if any data exists for the user in the selected month of a given year. Returns a str month.
       :param user: str
           The username of user of the current session
       :param year: str
           The year to check data for
       :return month: str
           The final month selected by user after validation
       """
    data = obtain_data(user)
    data_exists = False
    while not data_exists:
        if month.isnumeric():
            for item in data:
                if f"{year}-" in item[0]:
                    if f"-{int(month):02d}-" in item[0]:
                        data_exists = True
                        break
            if data_exists:
                return month
        print(f"{ansi.get('red')}Error. The month you selected has no data, or you have entered a non-numeric value.{ansi.get('reset')}")
        month = input("Choose a month to view data for: ")


def validate_float(user_input: str) -> bool:
    """Takes a str user input and checks if it is a valid float. Returns a bool.
    :param user_input: str
        The user input to be validated
    :return: bool
        True if user input is a valid float, False if user input is not a valid float
    """

    try:
        float(user_input)
        return True
    except ValueError:
        return False


def try_login() -> tuple:
    """Takes user input for username and password, and checks if the username and password is in one line in users.csv. Returns a tuple containing a bool and a str.
    :return: tuple
        A tuple containing a bool and a str. The bool is True if the username and password exist together, and False if the username and password do not match existing data. The str is the username of the user.
    """

    print(f"{ansi.get('bold')}[Log-in]{ansi.get('reset')}")
    with open('users.csv', mode='r') as f:
        # Reads the csv file containing the usernames and passwords
        data = f.readlines()
    success = False

    in_name = input("Enter your username: ")
    in_pass = input("Enter your password: ")

    for line in data:
        uname = line.split(',')[0]
        upass = line.split(',')[1].strip()  # strip() removes \n for any string unless specified

        if uname == in_name and upass == in_pass:  # user input matches an existing username and corresponding password
            success = True
            break

    return success, uname  # success of login, uname of current session user


def create_user():
    """Creates a new user and adds the user to users.csv."""

    print(f"{ansi.get('bold')}[Create New User]{ansi.get('reset')}")
    with open('users.csv', mode='r') as users_list:
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
            new_pass = input(f"{ansi.get('red')}Passwords do not match.{ansi.get('reset')}Create a password: ")
            confirm_new_pass = input("Confirm new password: ")
        else:
            break
    with open('users.csv', mode='a') as users_list:
        # Adds to the csv file the new user's details
        writer = csv.writer(users_list)
        writer.writerow([new_name, new_pass])
    with open(f"{new_name}.csv", mode='a') as user_data:
        # Creates the csv file that stores the new user's transactions
        writer = csv.writer(user_data)
        writer.writerow([datetime.date.today(), 0, "other"])


def create_transaction(select: int, name: str, categories: list):
    """Creates a new transaction and adds the transaction to the user's csv file.
    :param select: int
        The user's selection of transaction type
    :param name: str
        The username of the user of the current session
    :param categories: list
        A list containing strings of categories for deposits for the user to select from
    """
    action_date = datetime.date.today()
    if select == 1:  # User Create Transaction
        print(f"{ansi.get('bold')}[New Deposit]{ansi.get('reset')}")
        raw_dep = input("Enter amount of DAI you would like to deposit: ")
        while not validate_float(raw_dep):
            raw_dep = input(f"{ansi.get('red')}Error. Please enter how much DAI you would like to deposit: {ansi.get('reset')}")
        action_value = float(raw_dep)
        category = "deposit"
    if select == 2:
        print(f"{ansi.get('bold')}[New Withdrawal]{ansi.get('reset')}")
        raw_wtd = input("Enter amount of DAI you would like to withdraw: ")
        while not validate_float(raw_wtd):
            raw_wtd = input(f"{ansi.get('red')}Error. Please enter how much DAI you would like to deposit: {ansi.get('reset')}")
        action_value = float(raw_wtd)
        print(sr)
        print("Select a Category for your Withdrawal:")
        display_menu(categories)
        category = categories[validate_selection(categories)-1].lower()  # list index starts at 0 therefore -1

    with open(f"{name}.csv", 'a') as user_data:
        # Adds to the user's csv file the new transaction
        user_data.writelines(f"{action_date},{action_value},{category}\n")
    print(f"{ansi.get('green')}{ansi.get('bold')}Transaction Recorded: On {action_date}, {action_value} DAI as {category} on {name}'s wallet.{ansi.get('reset')}")


def obtain_data(name: str) -> list:
    """Obtains data from a user's csv file and returns a list of lists containing the data.
    :param name: str
        The username of the user of the current session
    :return: list
        A list of lists containing the transaction date, amount, and category from the user's csv file
    """

    with open(f'{name}.csv', mode='r') as user_list:
        # Reads the csv file containing the user's transaction data
        transaction_database = user_list.readlines()
    data = []
    for item in transaction_database:
        date, amount, category = item.strip().split(",")
        data.append([date, amount, category])
    return data


def find_scale(data: list) -> int:
    """Finds the scale of a bar chart based on the smallest value of the amount to be graphed.
    :param data: list
        A list of lists containing the transaction date, amount, and category from the user's csv file
    :return: int
        The scale of one symbol of the bar chart
    """

    data.sort()
    smallest = abs(data[0])
    multiple = 1
    while smallest//multiple > 10:
        multiple *= 10
    return multiple


def month_statistics(data: list, month: int, year: int):
    """Find the total profit and loss in a user specified month of a user specified year.
    :param data: list
        A list of lists containing the transaction date, amount, and category from the user's csv file
    :param month: int
        The month to check data for
    :param year: int
        The year to check data for
    :return: list
        A list containing the total profit and loss in a specified month of a specified year
    """

    profit = 0
    loss = 0
    for item in data:
        if f"{year}-{month:02d}-" in str(item[0]):
            if item[2] == 'deposit':
                profit += float(item[1])
            else:
                loss += float(item[1])
    return [profit, loss]


def month_spending(data: list, month: int, year: int) -> list:
    """Find the total spending in each category in a user specified month of a user specified year.
    :param data: list
        A list of lists containing the transaction date, amount, and category from the user's csv file
    :param month: int
        The month to check data for
    :param year: int
        The year to check data for
    :return: list
        A list containing the total spending in each category in a specified month of a specified year
    """

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


def create_bar(title: str, category: list, amounts: list, scale: int) -> str:
    """Creates a bar chart based on the title, category, amounts, and scale provided.
    :param title: str
        The title of the bar chart
    :param category: list
        A list containing strings of categories of each bar in the bar chart
    :param amounts: list
        A list containing the amounts for each category in the bar chart
    :param scale: int
        The scale of the amount one symbol represents in the bar chart
    :return: str
        A string containing the bar chart
    """

    bar_chart = f"{title}\n"
    for i in range(len(category)):
        amount_bar = abs(amounts[i]) // scale
        bar_category = f"{ansi.get('bold')}{category[i].ljust(20)}{ansi.get('reset')}"
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

ansi = {
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