logo = """

 __     __     ______     __         __         ______     ______  
/\ \  _ \ \   /\  __ \   /\ \       /\ \       /\  ___\   /\__  _\ 
\ \ \/ ".\ \  \ \  __ \  \ \ \____  \ \ \____  \ \  __\   \/_/\ \/ 
 \ \__/".~\_\  \ \_\ \_\  \ \_____\  \ \_____\  \ \_____\    \ \_\ 
  \/_/   \/_/   \/_/\/_/   \/_____/   \/_____/   \/_____/     \/_/ 
                                                                   

"""

main_menu = f"""
{"create new transaction".title().ljust(50, '.')} type 1\n
{"view past transactions".title().ljust(50, '.')} type 2\n
{"view description of DAI currency".title().ljust(50, '.')} type 3\n
{"log out".title().ljust(50, '.')} type 4\n
"""

main_menu = ["create new transaction".title(), "view past transactions".title(), "view description of DAI currency".title(), "log out".title()]
startup = ['Already have an account? Log-in', 'New user? Sign-up']


def display_menu(choices: list)-> str:
    menu = ''
    count = 1
    for it in choices:
        menu += f"{menu.ljust(50, '.')} type {count}\n"
        count += 1
    return menu


def validate_selection(choices: list) -> int:
    expect = len(choices)
    select = int(input(f'Select a choice between 1~{expect}'))
    while not 0 < select < expect+1:
        select = int(input(f'Error. Please select a choice between 1~{expect}'))
    return select


def select_user_menu():
    print(logo)
    print(ask_at_startup)
    select = int(input("Choose a function by typing a number 1~2: "))



def select_main_menu() -> int: #The int return number is each function/next menu
    print("Welcome to your wallet!".upper()) #TODO: Add color to this
    print(main_menu)
    select = int(input("Choose a function by typing a number 1~4: "))
    while select > 4 or select < 1:
        select = int(input("Error. Please choose a function by typing a number 1~4: "))
    return select
#
#
# if print_menu() == 1:
#     pass
#     # call function()
# elif print_menu() == 2:
#     pass
#     # call function()
# elif print_menu() == 3:
#     pass
#     # call function
# elif print_menu() == 4:
#     pass
#     # call function
# else:
#     print("Error. An unexpected error occured. Please try again.")