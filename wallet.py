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

from menu import display_menu, validate_selection, logo
startup = ['Already have an account? Log-in', 'New user? Sign-up']

print(logo)
print("Welcome to your WALLET!") # TODO: Colors! Banners! Yay!

# Log-in or Create User
print(display_menu(startup))
selection = validate_selection(startup)
if selection == 1: # User wants to log-in
    in_name = input("Enter your username: ")
    in_pass = input("Enter your password: ")
    success = try_login(in_name, in_pass)
    while success == False:
        print("Wrong username or password. Try again.")
        in_name = input("Enter your username: ")
        in_pass = input("Enter your password: ")
        try_login(in_name, in_pass)