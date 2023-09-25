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

def create_transaction(select: int, name: str):
    action_date = datetime.date.today()
    if select == 1:  # User Create Transaction
        raw_dep = input("Enter amount of DAI you would like to deposit: ")
        while not raw_dep.isdigit():
            raw_dep = input("Error. Please enter as a numeric value how much DAI you would like to deposit: ")
        action_value = float(raw_dep)
    if select == 2:
        raw_wtd = input("Enter amount of DAI you would like to withdraw: ")
        while not raw_wtd.isdigit():
            raw_wtd = input("Error. Please enter as a numeric value how much DAI you would like to withdraw: ")
        action_value = -(float(raw_wtd))
    with open(f"{name}.csv", 'a') as user_data:
        user_data.writelines(f"{action_date},{action_value}\n")


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
