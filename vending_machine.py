#NAME: Wenjia Liu
#STUDENT ID: 260919690

import sys

TOONIES = 5     #The machine has $25 distributed as follows: $10 in toonies, 5 in loonies, 5 in quarters, 3 in dimes, 2 in nickels. 
LOONIES = 5     #Due to the fact that the change will be composed of toonies($2), loonies($1), quarters($0.25), dimes($0.10), and nickels($0.05).
QUARTERS = 20   #Therefore, the machine has the number of coins available as follows: 5 toonies, 5 loonies, 20 quarters, 30 dimes and 40 nickels.
DIMES = 30
NICKELS = 40

def display_welcome_menu():
    """ display the full menu. """

    print()
    print("Welcome to the COMP 202 virtual Vending Machine.")
    print("Here are your options:")
    print("1. Candy bar $2.95")
    print("2. Cookies $3.95")
    print("3. Soda $4.00")
    print("4. Chips $3.90")
    print("5. No snacks for me today!")
    print()

def get_snack_price(option):
    """ (num) -> num
    Returns the price in cents of option
    >>> get_snack_price(1)
    295
    >>> get_snack_price(2)
    390
    >>> get_snack_price(3)
    400
    >>> get_snack_price(4)
    390
    >>> get_snack_price(5)
    0
    """
    if (option == 1):     #Once the choice has been made
        return 295        #return the price in cents according to the choice made.
    if (option == 2 or option == 4):
        return 390
    if (option == 3):
        return 400
    return 0

def get_num_of_coins(amount,cent_of_coin,num_of_available_coin):
    """ (num, num, num) -> num
    Returns the maximum number of coins of cent_of_coin that can
    be used to work toward achieving the amount
    >>> get_num_of_coins(1000, 100, 8)
    8
    >>> get_num_of_coins(600,100,8)
    6
    >>> get_num_of_coins(600,30,20)
    20
    >>> get_num_of_coins(1000,200,4)
    4
    """
    num_of_need_coin = amount//cent_of_coin
    if num_of_need_coin < num_of_available_coin:
        return num_of_need_coin
    return num_of_available_coin

def compute_and_display_change(amount_of_change):
    """ (num) -> bool
    This function takes one non-negative integer representing the
    change in cents that the vending machine should give back to
    the customer and computes the most convenient exact change.If
    the machine has enough coins to make the change,then the function
    displays the corresponding information on the sceen and return True.
    Otherwose,the function must not display anything and returns Flase.
    >>> compute_and_display_change(185)
    Here is your change:
    toonies x 0
    loonies x 1
    quarters x 3
    dimes x 1
    nickels x 0

    True
    >>> compute_and_display_change(100)
    Here is your change:
    toonies x 0
    loonies x 1
    quarters x 0
    dimes x 0
    nickels x 0

    True
    >>> compute_and_display_change(594)
    False
    >>> compute_and_display_change(2900)
    False
    """
    if (amount_of_change > 2500):
        return False
    if (amount_of_change % 5 > 0):
        return False
    toonies = get_num_of_coins(amount_of_change,200,TOONIES)
    amount_of_change -= (200*toonies)
    loonies = get_num_of_coins(amount_of_change,100,LOONIES)
    amount_of_change -= 100 *loonies
    quarters = get_num_of_coins(amount_of_change,25,QUARTERS)
    amount_of_change -= 25 *quarters
    dimes = get_num_of_coins(amount_of_change,10,DIMES)
    amount_of_change -= 10 *dimes
    nickels = get_num_of_coins(amount_of_change,5,NICKELS)
    print("Here is your change:")
    print("toonies x %d" % toonies)
    print("loonies x %d" % loonies)
    print("quarters x %d" % quarters)
    print("dimes x %d" % dimes)
    print("nickels x %d\n" % nickels)
    return True

#helper function
def get_choice():
    """
    This function get the choice and returns the price in cents
    of the choice
    >>> get_choice()
    Please select your choice: 1
    The item of your choice costs 295 cents

    295
    >>> get_choice()
    Please select your choice: 2
    The item of your choice costs 295 cents

    390
    >>> get_choice()
    Please select your choice: 3
    The item of your choice costs 295 cents

    400
    >>> get_choice()
    Please select your choice: 4
    The item of your choice costs 295 cents

    390
    >>> get_choice()
    Please select your choice: 5
    The item of your choice costs 295 cents

    0
    """
    choice = int(input("Please select your choice: "))
    price_of_choice = get_snack_price(choice)
    if (price_of_choice == 0):
        print("Nothing for you today. Thank you for stopping by!")
        return 0
    print("The item of your choice costs %d cents\n" % price_of_choice)
    return price_of_choice

#helper function
def get_money():
    """
    Returns the money in cents that the customer has input
    >>> get_money()
    Enter your money: $7.44
    You inserted 744 cents

    744
    >>> get_money()
    Enter your money: $7.444444
    You inserted 744 cents

    744
    >>> get_money()
    Enter your money: $5.66678
    You inserted 567 cents

    567
    """
    money = round(float(input("Enter your money: $")),2)
    money_in_cents = int(100 * money)
    print("You inserted %d cents\n" % money_in_cents)
    return money_in_cents

#helper function    
def do_change(change):
    """
    After computing and displaying the change to be provided, if the machine has enough coins to make the change, then the function will displays the corresponding information on the screen and returns True.
    Otherwise, the function must not display anything and returns False.
    >>> b = compute_and_display_change(125)
    Here is your change:
    toonies x 0
    loonies x 1
    quarters x 1
    dimes x 0
    nickels x 0
   
    >>> b
    True
    
    >>> b = compute_and_display_change (3600)
    >>> b
    
    False
    >>> b = compute_and_display_change(122)
    >>> b
    
    False
    """
    print("You should receive back %d cents" % change) 
    b = compute_and_display_change(change)
    if b:
        print("It was a pleasure doing business with you")   #After paying the money, the machine will display a goodbye message.
    else:
        print("The machine does not have enough coins for your change.Come by another time!")

def operate_machine():
    """
    Performs the following tasks in the following order:
    displays the menu
    gets the user choice
    handles the choice
    gets the money in $ and displays it in cents
    print information according the value of money
    displays the change in cents
    computes the change and displays the change
    >>> operate_machine()
    Welcome to the COMP 202 virtual Vending Machine.
    Here are your options:
    1. Candy bar $2.95
    2. Cookies $3.95
    3. Soda $4.00
    4. Chips $3.90
    5. No snacks for me today!

    Please select your choice: 5
    Nothing for you today. Thank you for stopping by!
    operate_machine()
    Welcome to the COMP 202 virtual Vending Machine.
    Here are your options:
    1. Candy bar $2.95
    2. Cookies $3.95
    3. Soda $4.00
    4. Chips $3.90
    5. No snacks for me today!

    Please select your choice: 2
    The item of your choice costs 390 cents

    Enter your money: $3.88
    You inserted 388 cents

    We do not accept pennies.Come by another time!
    >>> operate_machine()
    Welcome to the COMP 202 virtual Vending Machine.
    Here are your options:
    1. Candy bar $2.95
    2. Cookies $3.95
    3. Soda $4.00
    4. Chips $3.90
    5. No snacks for me today!

    Please select your choice: 2
    The item of your choice costs 390 cents

    Enter your money: $3.35
    You inserted 335 cents

    You do not have enough money.Come by another time!
    >>> operate_machine()
    Welcome to the COMP 202 virtual Vending Machine.
    Here are your options:
    1. Candy bar $2.95
    2. Cookies $3.95
    3. Soda $4.00
    4. Chips $3.90
    5. No snacks for me today!

    Please select your choice: 1
    The item of your choice costs 295 cents

    Enter your money: $3.35
    You inserted 335 cents

    You should receive back 40 cents
    Here is your change:
    toonies x 0
    loonies x 0
    quarters x 1
    dimes x 1
    nickels x 1

    It was a pleasure doing business with you
    
    """
    display_welcome_menu()
    price = get_choice()
    if price == 0:
        return
    money_in_cents = get_money()
    if money_in_cents%5 > 0:
        print("We do not accept pennies.Come by another time!")
        return
    if money_in_cents < price:
        print("You do not have enough money.Come by another time!")
        return
    change = money_in_cents-price
    do_change(change)
    
if (__name__ == "__main__"):
    operate_machine()
    

