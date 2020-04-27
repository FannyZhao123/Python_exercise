#NAME: Wenjia Liu
#STUDENT ID: 260919690

import math

def display_welcome_menu():
    '''display the full menu.'''
    
    print()
    print("Welcome to the COMP 202 fair pizza caculator !")
    print("Please chose one of the following modes:")
    print("A. \"Quantity mode\"")
    print("B. \"Price mode\"")
    print()
    
def get_fair_quantity(d1,d2):
    ''' (num,num) -> num
    Takes two positive integers representing the diameters of two
    pizzas and returns an integer indicating the minimum number of
    smaller pizzas Johnny must order to get at least the same anount
    of pizza as one large pizza
    >>> get_fair_quantity(12,4)       
    9
    >>> get_fair_quantity(12,5)
    6
    >>> get_fair_quantity(5,12)
    6
    >>> get_fair_quantity(5,5)
    1
    '''
    if (d1==d2):
        return 1
    s1 = get_pizza_area(d1)
    s2 = get_pizza_area(d2)
    if (d1<d2):                 #when the first pizza is smaller than second one
        return math.ceil(s2/s1) #return the smallest number of first pizza required.
    else:                       #when the first pizza is bigger than second one
        return math.ceil(s1/s2) #return the smallest number of second pizza required.
        
def get_fair_price(large_d,large_p,small_d,small_count):
    """
    Returns the total price Johnny should be paying to buy the smaller pizzas such that the amount of pizza per dollar is the same as that of the larger pizza.
    >>> get_fair_price(7, 7, 7, 7)
    49
    
    >>> get_fair_price(5, 5, 1, 1)
    0.2
     
    >>> get_fair_price(12, 10.0, 6, 2)
    5.0
    """
    large_area = get_pizza_area(large_d)
    p_per_dollar = large_p/large_area
    small_area = get_pizza_area(small_d)
    fair_p = small_area*small_count*p_per_dollar
    return round(fair_p,2)  #return the value that must be a real number with no more than 2 digits after the decimal point.

#helper function
def get_pizza_area(d):
    '''(num) -> num
    Returns a value proportional to the area of pizza of diameters of d
    >>> get_pizza_area(3)
    9
    >>> get_pizza_area(4)
    16
    >>> get_pizza_area(5)
    25
    '''
    return d*d

#helper function
def handle_mode_a():
    '''
    >>> handle_mode_a()
    You selected "Quantity mode"

    Enter the diameter of large pizza: 13
    Enter the diameter of small pizza: 3

    To be fully satisfied you should order 19 small pizzas
    >>> handle_mode_a()
    You selected "Quantity mode"

    Enter the diameter of large pizza: 8
    Enter the diameter of small pizza: 3

    To be fully satisfied you should order 8 small pizzas
    >>> handle_mode_a()
    You selected "Quantity mode"

    Enter the diameter of large pizza: 3
    Enter the diameter of small pizza: 8

    To be fully satisfied you should order 8 small pizzas
    '''
    print('You selected \"Quantity mode\"')
    print()
    large_d = int(input('Enter the diameter of large pizza: '))
    small_d = int(input('Enter the diameter of small pizza: '))
    small_count = get_fair_quantity(large_d,small_d)
    print()
    print('To be fully satisfied you should order',small_count,'small pizzas')
    

def handle_mode_b():
    '''
    >>> handle_mode_b()
    You selected "Price mode"

    Enter the diameter of large pizza: 13
    Enter the price of large pizza: 11
    Enter the diameter of small pizza: 3
    Enter the number of small pizzas you'd like to buy: 4

    The fair price to pay for 4 small pizzas is $2.34
    >>> handle_mode_b()
    You selected "Price mode"

    Enter the diameter of large pizza: 16
    Enter the price of large pizza: 14
    Enter the diameter of small pizza: 8
    Enter the number of small pizzas you'd like to buy: 5

    The fair price to pay for 5 small pizzas is $17.5
    >>> handle_mode_b()
    You selected "Price mode"

    Enter the diameter of large pizza: 16
    Enter the price of large pizza: 7
    Enter the diameter of small pizza: 4
    Enter the number of small pizzas you'd like to buy: 5

    The fair price to pay for 5 small pizzas is $2.19
    '''
    print('You selected \"Price mode\"')
    print()
    large_d = int(input('Enter the diameter of large pizza: '))
    large_p = float(input('Enter the price of large pizza: '))
    small_d = int(input('Enter the diameter of small pizza: '))
    small_count = int(input('Enter the number of small pizzas you\'d like to buy: '))
    fair_p = get_fair_price(large_d,large_p,small_d,small_count)
    print()
    print('The fair price to pay for' , small_count, 'small pizzas is $'+str(fair_p))

def run_pizza_caculator():
    """
    Performs the following tasks in the following order:
    >>> run_pizza_caculator()
    Welcome to the COMP 202 fair pizza caculator !
    Please chose one of the following modes:
    A. "Quantity mode"
    B. "Price mode"

    Enter your choice: A

    You selected "Quantity mode"

    Enter the diameter of large pizza: 14
    Enter the diameter of small pizza: 6

    To be fully satisfied you should order 6 small pizzas
    
    >>> run_pizza_caculator()
    Welcome to the COMP 202 fair pizza caculator !
    Please chose one of the following modes:
    A. "Quantity mode"
    B. "Price mode"

    Enter your choice: B

    You selected "Price mode"

    Enter the diameter of large pizza: 12
    Enter the price of large pizza: 9.33
    Enter the diameter of small pizza: 8
    Enter the number of small pizzas you'd like to buy: 2

    The fair price to pay for 2 small pizzas is $8.29
    
    >>> run_pizza_caculator()
    Welcome to the COMP 202 fair pizza caculator !
    Please chose one of the following modes:
    A. "Quantity mode"
    B. "Price mode"

    Enter your choice: B

    You selected "Price mode"

    Enter the diameter of large pizza: 8
    Enter the price of large pizza: 2
    Enter the diameter of small pizza: 2
    Enter the number of small pizzas you'd like to buy: 2

    The fair price to pay for 2 small pizzas is $0.25 
    """
    
    display_welcome_menu();
    choice = input('Enter your choice: ')
    print()
    if (choice == 'A'):
        handle_mode_a()
    elif (choice == 'B'):
        handle_mode_b()
    else:
        print('This mode is not supported')
    
if (__name__ == "__main__"):
    run_pizza_caculator()
   

