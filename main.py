from login import try_login, create_user
from menu import print_start, print_menu
from login import create_user

selection = 0
print_start()
selection = input("Choose option by typing in the number of the menu: ")

if selection == 1:
    in_name = input("Enter your username: ")
    in_pass = input("Enter your password: ")
    result = try_login(name=in_name, password=in_pass)

    while (result is False):
        print("Username or Password is wrong. Try again.")
        in_name = input("Enter your username: ")
        in_pass = input("Enter your password: ")
        result = try_login(name=in_name, password=in_pass)

# End of log-in


# with open('users.csv', mode='r') as f:
#     data = f.readlines()
#     for line in data:
#         name, passw = line.strip().split(',')
# for users in name:
#     with open(f'{users}.csv', mode='a') as f:


