logo = """

 __     __     ______     __         __         ______     ______  
/\ \  _ \ \   /\  __ \   /\ \       /\ \       /\  ___\   /\__  _\ 
\ \ \/ ".\ \  \ \  __ \  \ \ \____  \ \ \____  \ \  __\   \/_/\ \/ 
 \ \__/".~\_\  \ \_\ \_\  \ \_____\  \ \_____\  \ \_____\    \ \_\ 
  \/_/   \/_/   \/_/\/_/   \/_____/   \/_____/   \/_____/     \/_/ 
                                                                   

"""

start_menu = f"""
{"create new transaction".title().ljust(50, '.')} type 1\n
{"view past transactions".title().ljust(50, '.')} type 2\n
{"view description of DAI currency".title().ljust(50, '.')} type 3\n
{"log out".title().ljust(50, '.')} type 4\n
"""
def print_start():
    print(logo)
def print_menu() -> int: #The int return number is each function/next menu
    print("Welcome to your wallet!".upper()) #TODO: Add color to this
    print(start_menu)
    select = int(input("Choose a function by typing a number 1~4: "))
    while select > 4 or select < 1:
        select = int(input("Error. Please choose a function by typing a number 1~4: "))
    return select

if print_start() == 1:
    # call function()
elif print_start() == 2:
    # call function()
elif print_start() == 3:
    # call function
elif print_start() == 4:
    # call function
else:
    print("Error. An unexpected error occured. Please try again.")