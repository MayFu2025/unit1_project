from menu import display_menu, validate_selection
from wallet import ask_return
from wallet import name
action_menu = ["Deposit", "Withdraw"]

def return_back():
    display_menu(ask_return)
    choice = validate_selection(ask_return)
    if choice == 1:
        return True
    if choice == 2:
        return False


def main_functions(selection):
    if selection == 1:
        display_menu(action_menu)
        choice = validate_selection(action_menu)
        if choice == 1:
            raw_dep = input("Enter amount of DAI you would like to deposit: ")
            while not raw_dep.isnumeric():
                raw_dep = raw_dep = input("Error. Please enter as a numeric value how much DAI you would like to deposit: ")
            deposit = int(raw_dep)
        with open(f"{name}.csv", 'a') as myfile:
            myfile.writelines(f",\n")
        back_to_menu = return_back()

    if selection == 2:
        pass

    if selection == 3:
        print()

    if selection == 4:
        pass