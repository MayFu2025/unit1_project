# Create a login function!

def try_login(name: str, password: str) -> bool:
    with open('users_lesson_0914.csv', mode='r') as f:
        data = f.readlines()

    success = False
    for line in data:
        uname = line.split(',')[0]
        upass = line.split(',')[1].strip()  # strip() removes \n for any string unless specified

        if uname == name and upass == password:
            success = True
            break

    return success


# Testing
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

if result is False:
    print('Too many failed attempts. Sayonara!')
    exit(1)  # 1 is the code for exit without error

# The program continues here if it doesn't close
print("Welcome")