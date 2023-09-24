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

def try_login() -> bool:
    '''Tests if user can successfully log in. Returns a boolean on success of log-in.'''
    with open('users.csv', mode='r') as f:
        data = f.readlines()
    success = False

    in_name = input("Enter your username: ")
    in_pass = input("Enter your password: ")

    for line in data:
        uname = line.split(',')[0]
        upass = line.split(',')[1].strip()  # strip() removes \n for any string unless specified
        while uname != in_name and upass != in_pass:
            print("Wrong username or password. Try again.")
            in_name = input("Enter your username: ")
            in_pass = input("Enter your password: ")
        success = True
    return success

def create_user():
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
    with open(f"{new_name}.csv", 'a') as user_data:
        user_data.writelines(f"{datetime.date.today()},0\n")