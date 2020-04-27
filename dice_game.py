#Name: Wenjia Liu
#ID: 260919690

import random

def dice_roll():
    '''
    When the game starts, roll the dice twice, then add them up, return the value will be between 2 and 12(included).
    >>> random.seed(4)
    >>> dice_roll()
    5
    >>> dice_roll()
    7
    
    
    >>> random.seed(3)
    >>> dice_roll()
    7
    >>> dice_roll()
    7
    
    
    >>> random.seed(6)
    >>> dice_roll()
    6
    >>> dice_roll()
    7
    '''
    x = random.randint(1, 6)            #x represents the first dice
    y = random.randint(1, 6)            #y represents the second dice 
    return x + y
 
 
 
 
def second_stage(point):
    '''
    Return an integer which will either be a 7 or the point itself depending on which one gets rolled first. Otherwise, the game will continue before either a 7 or the point is rolled. 
    >>> random.seed(8)
    >>> r = second_stage(9)
    5 6 8 2 4 7
    >>> r
    7
    
    >>> random.seed(234)
    >>> r = second_stage(8)
    6 6 9 10 5 6 9 4 8 
    >>> r
    8
    
    >>> random.seed(789)
    >>> r = second_stage(8)
    10 7
    >>> r
    7 
   
    '''
        
    x = dice_roll()
    
    while(x!= 7 and x!= point):
        print("%d" % x, end = ' ')
        x = dice_roll()                      #update x

    if (point == x):
        print(x)
        return x

    elif (x == 7): 
        print(7)
        return 7
   
     
 
def can_play(own, bet):
    '''
    This function takes two floats as input and returns a boolean value. The first one represents the money that player has,
    the second one is the money that the player would like to bet. The only condition to allow the player to play is the money they bet more than $0.0, but not more than what they own.
    The function will return True if the player is allowed to play, otherwise it returns False.
    >>> can_play(9.3, 11.4):
    False
    
    >>> can_play(10.0, 5.5):
    True
    
    >>> can_play(5.5, 2.2):
    True

    '''
    if (bet > 0 and bet <= own):
        return True
    
    else:
        return False
    



def pass_line_bet(total, decide_to_bet):

    '''
    The function It takes two floats as input: the first one corresponds the total amount of money the player has, the second correspond to how much money the player decides to bet.
    The function will display the result of Come-Out Roll as well as what will happen next.
    The message that indicates what will happen next contains 3 possible outcomes:
    1. You win!
    2. You lose!
    3. Roll again!
    Then the function will return a float which corresponds to the amount of money the player has left after one round of Craps.
    >>> random.seed(6)
    >>> m = pass_line_bet(11.5, 2.5)
    A 6 has been rolled. Roll again!
    7
    You lose!
    >>> m
    9.0
    

    >>> random.seed(5)
    >>> m = pass_line_bet(12.5, 3.5)
    A 8 has been rolled. Roll again!
    9 12 11 5 8
    You win!
    >>> m
    16.0
    

    >>> random.seed(3)
    >>> m = pass_line_bet(5.0, 5.0)
    A 7 has been rolled. You win!
    >>> m
    10.0


    '''
        
    point = dice_roll()
    if (point == 7 or point == 11):
        print("A %d has been rolled. You win!" % point)
        win = total + decide_to_bet
        return win
    
    elif (point == 2 or point == 3 or point == 12):
        print("A %d has been rolled. You lose!" % point)
        lose = total - decide_to_bet
        return lose
    
    else:
        print("A %d has been rolled. Roll again!" % point)
        second_roll = second_stage(point)
        
        if (second_roll == 7):
            print("You lose!")
            lose = total - decide_to_bet
            return lose
        
        elif (second_roll == point):
            print("You win!")
            win = total + decide_to_bet
            return win



def play():
 
    '''
    The function retrieves two inputs from the user. The first input corresponds to the money the player has,
    the second to the money they would like to bet. If the user does not have enough money to play,
    the function displays a message informing the user about it and terminates.
    Otherwise, the function will place the bet.
    At last, the function will display a statement indicating the player about the money they have left after their bet,
    note that the number representing the money left should not have more than 2 decimals.
    
    >>> random.seed(8)
    >>> play()
    Please enter your money here: 10.0
    How much would you like to bet? 3.5
    A 9 has been rolled. Roll again!
    6 8 2 4 7
    You lose!
    You now have $ 6.50


    >>> random.seed(999)
    >>> play()
    Please enter your money here: 10.0
    How much would you like to bet? 10.0
    A 7 has been rolled. You win!
    You now have $ 20.00

    >>> play()
    Please enter your money here: 4.0
    How much would you like to bet? 8.0
    Insufficient funds. You cannot play.

    '''
    money_user_have = float(input("Please enter your money here: "))        #enter the total money I have
    user_like_to_bet = float(input("How much would you like to bet? "))     #the money I would like to bet
    able_to_play = can_play(money_user_have, user_like_to_bet)              #test whether the player can start the game or not 

    if (able_to_play == False): 
        print ("Insufficient funds. You cannot play.")
    else:
        left = pass_line_bet (money_user_have, user_like_to_bet)            #the money left after the first round
        print ("You now have $ %.2f" % left)                                  #the money that the player left 
            
        
     
        
        
        
        
        
        
        
        
        
