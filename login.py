# Create a login function!
def try_login(name: str, password: str) -> bool:
    with open('users.csv', mode='r') as f:
        data = f.readlines()

    success = False
    for line in data:
        uname = line.split(',')[0]
        upass = line.split(',')[1].strip()  # strip() removes \n for any string unless specified

        if uname == name and upass == password:
            success = True
            break

    return success

def login_success() -> bool:
    in_name = input("Enter your username: ")
    in_pass = input("Enter your password: ")
    success = try_login(in_name, in_pass)
    return success


def login_function() -> tuple:
    in_name = input("Enter your username: ")
    in_pass = input("Enter your password: ")
    success = try_login(in_name, in_pass)
    while success == False:
        print("Wrong username or password. Try again.")
        in_name = input("Enter your username: ")
        in_pass = input("Enter your password: ")
        success = try_login(in_name, in_pass)
    return success, in_name

# # test logging-in
# attempts = 3
#
# in_name = input("Enter your username: ")
# in_pass = input("Enter your password: ")
# result = try_login(name=in_name, password=in_pass)
#
# while (result is False) and (attempts > 1):
#     print("Username or Password is wrong. Try again.")
#     in_name = input("Enter your username: ")
#     in_pass = input("Enter your password: ")
#     result = try_login(name=in_name, password=in_pass)
#     attempts -= 1
#
# if result is False:
#     print('Too many failed attempts. Sayonara!')
#     exit(1)  # 1 is the code for exit without error
#
# # The program continues here if it doesn't close
# print("Welcome")



# Create a create new account option!
import csv
def create_user():
    with open('users.csv', mode='r') as users_list:
        users_database = users_list.readlines()
    new_name = input("Create a username: ")
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
    # TODO: if a user that has just created their account goes to the menu and pick stats, the user's own csv file does not yet exist until they input their first transaction. Would it be better to create it here?






# test creation of new user:
# create_user()


# # Log-in
#
# attempts = 3
#
# in_name = input("Enter your username: ")
# in_pass = input("Enter your password: ")
# result = try_login(name=in_name, password=in_pass)
#
# while (result is False) and (attempts > 1):
#     print("Username or Password is wrong. Try again.")
#     in_name = input("Enter your username: ")
#     in_pass = input("Enter your password: ")
#     result = try_login(name=in_name, password=in_pass)
#     attempts -= 1
#
# # End of log-in