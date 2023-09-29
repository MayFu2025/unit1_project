# Crypto Wallet

![](22ROOSE-master768.gif)  
<sub>Illustration for Glenn Harvey</sub>

# Criteria A: Planning

## Problem definition

Ms. Sato is a local trader who is interested in the emerging market of cryptocurrencies. She has started to buy and sell electronic currencies, however at the moment she is tracking all his transaction using a ledger in a spreadsheet which is starting to become burdensome and too disorganized. It is also difficult for Ms Sato to find past transactions or important statistics about the currency. Ms Sato is in need of a digital ledger that helps her track the amount of the cryptocurrency, the transactions, along with useful statistics. 

Apart for this requirements, Ms Sato is open to explore a cryptocurrency selected by the developer.

An example of the data stored is 

| Date | Description | Category | Amount  |
|------|-------------|----------|---------|
| Sep 23 2022 | bought a house | Expenses | 10 BTC |
| Sep 24 2022 | food for house celebration | Food | 0.000001 BTC |


## Proposed Solution

Design statement:
I will to design and make a digital ledger / electronic wallet for a client who is Ms. Sato as per the Problem definition. The ——– will about ———— and is constructed using the software PyCharm. It will take  approximately a month to make and will be evaluated according to the success criteria listed below.

#** add a description of your coin and citation **

I will be making the electronic wallet on PyCharm, and it will be run in the Terminal for use. I will be using PyCharm to code the product, as PyCharm is a suitable IDE for coding while also being able to display outputs in the terminal. The wallet should be able to run on the Terminal, as per the client's (Ms. Sato) request (See success criteria below).

## Success Criteria
1. The electronic ledger is a text-based software (Runs in the Terminal). (Pre-determined success criteria)
2. The electronic ledger display the basic description of the cyrptocurrency selected. (Pre-determined success criteria)
3. The electronic ledger allows to enter, withdraw and record transactions. (Pre-determined success criteria)
4. The electronic ledger can display statistics such as profit, total spendings, total earnings, and balance.
5. The electronic ledger organizes transactions based on categories such as "Expenses," "Food," "Clothes," etc.
6. The electronic ledger is password protected.

# Criteria B: Design

## System Diagram
![](unit1_system_diagram.jpg)
*fig.1* System diagram of proposed solution
## Flow Diagrams


## Record of Tasks
| Task No | Planned Action        | Planned Outcome                                                                          | Time estimate | Target completion date | Criterion |
|---------|-----------------------|------------------------------------------------------------------------------------------|---------------|------------------------|-----------|
| 1       | Create system diagram | To have a clear idea of the hardware and software requirements for the proposed solution | 10 min        | Sep 13                 | B         |
| 2       | Create a login system | To have a flow diagram and the code for the login system                                 | 30 min        | Sep 14                 | B, C      |

# Criteria C: Development

## Login System
My client requires a system to protect the private data. I thought about using a login system to accomplish this requirement using a if condition and the open command to work with a csv file.

In the first line, I define the function try_login. The try_login function takes two parameters. name, which is a string, and password, which is also a string. The function should have a boolean output representing True if the user logs in correctly, and False if they do not.

From the second line to the third line, I save the user information which is stored in a csv file as a variable called data. The user.csv file contains user log-in data as comma separated values (username),(password). The open function takes two parameters. First, the csv file for the function to open, and second, the mode of what the function will do with the csv file. The mode 'r' tells the program to read the content of the csv file opened. The line 'as f' saves the file as the variable f, making it easier call other functions with the csv file later. Using the function readlines(), the program saves each line of the file f as an item in the list 'data'.

From the fourth line to the final line, the program will use the data obtained in the previous lines to determine if the user may now log-in to the ledger or not. First, the variable success, which represents whether the user has successfully logged in or not, is defined. When first defined, success is a boolean, False. In the next line, a for loop is started, which will loop between every line (item in lsit, string) in data (list). 
```.py
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
```

## Creating a New User
