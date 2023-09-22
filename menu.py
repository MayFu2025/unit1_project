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

ask_at_startup = f"""
{'Already have an account? Log-in'.ljust(50, '.')} type 1\n
{'New user? Sign-up'.ljust(50, '.')} type 2\n
"""

def print_start():
    print(logo)
    print(ask_at_startup)



def print_menu() -> int: #The int return number is each function/next menu
    print("Welcome to your wallet!".upper()) #TODO: Add color to this
    print(start_menu)
    select = int(input("Choose a function by typing a number 1~4: "))
    while select > 4 or select < 1:
        select = int(input("Error. Please choose a function by typing a number 1~4: "))
    return select


if print_menu() == 1:
    pass
    # call function()
elif print_menu() == 2:
    pass
    # call function()
elif print_menu() == 3:
    pass
    # call function
elif print_menu() == 4:
    pass
    # call function
else:
    print("Error. An unexpected error occured. Please try again.")