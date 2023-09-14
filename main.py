from login import try_login

# Log-in

attempts = 3

in_name = input("Enter your username: ")
in_pass = input("Enter your password: ")
result = try_login(name=in_name, password=in_pass)

while (result is False) and (attempts > 1):
    print("Username or Password is wrong. Try again.")
    in_name = input("Enter your username: ")
    in_pass = input("Enter your password: ")
    result = try_login(name=in_name, password=in_pass)
    attempts -= 1

# End of log-in