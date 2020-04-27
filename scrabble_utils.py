#Name: Wenjia Liu 
#ID: 260919690

import doctest 
import random
from dicts_utils import *
from board_utils import *

def display_rack(rack_dict):
    """ (dict) -> none
    Displays one line containing the letters that are on the rack using upper case.
    
    >>> display_rack({'g': 1, 'k': 0, 'p': 4})
    G P P P P 
    >>> display_rack({'a': 1, 'b': 0, 'c': 1})
    A C 
    >>> display_rack({'a': 1, 'l': 1})
    A L 
    """
    for key in rack_dict:
        for i in range (rack_dict[key]):
            print (key.upper(), end=" ")


def has_letters(rack_dict, letter_str):
    """ (dict) -> bool
    Returns true if all the characters in the input string are available on the rack and if so, it removes those letters from the rack.
    Otherwise, returns false and does not modify the rack. 

    >>> rack_dict = {'a': 1, 'c': 1, 't': 1, 'r': 1}
    >>> has_letters(rack_dict, 'cat')
    True
    >>> rack_dict == {'r': 1}
    True
    
    >>> rack_dict = {'a': 1, 'k': 1, 't': 1, 'r': 1}
    >>> has_letters(rack_dict, 'cycle')
    False
    >>> rack_dict == {'a': 1, 'k': 1, 't': 1, 'r': 1}
    True
    
    >>> rack_dict = {'a': 1, 'k': 1, 't': 1, 'r': 1}
    >>> has_letters(rack_dict, 'rat')
    True
    >>> rack_dict == {'k': 1}
    True
    """
    new_dic = count_occurrences(letter_str)
    return subtract_dicts(rack_dict, new_dic)
    
    
def refill_rack(rack, pool, n):
    """ (dict, dict, int) -> none
    Draws letters at random from the pool and adds them to the rack
    until there are either n letters on the rack or no more letters in the pool. 
    
    >>> random.seed(6)
    >>> rack = {'a': 2, 'm': 1}
    >>> pool = {'a': 1, 'e': 2, 'h': 1, 'l': 2, 'n': 1, 'p': 2, 's': 3, 't': 2, 'z': 1}
    >>> refill_rack(rack, pool, 8)
    >>> rack
    {'a': 2, 'm': 1, 't': 1, 's': 1, 'e': 1, 'p': 1, 'l': 1}
    >>> pool
    {'a': 1, 'e': 1, 'h': 1, 'l': 1, 'n': 1, 'p': 1, 's': 2, 't': 1, 'z': 1}
 
    >>> random.seed(9)
    >>> rack = {'a': 2, 'k': 1}
    >>> pool = {'a': 1, 'e': 2, 's': 3, 't': 2, 'z': 1}
    >>> refill_rack(rack, pool, 10)
    >>> rack
    {'a': 3, 'k': 1, 't': 2, 's': 2, 'e': 2}
    >>> pool
    {'s': 1, 'z': 1}
    
    >>> random.seed(8)
    >>> rack = {'a': 2, 'k': 1}
    >>> pool = {'h': 1, 'e': 2, 'k': 3, 'm': 2, 'q': 1}
    >>> refill_rack(rack, pool, 10)
    >>> rack
    {'a': 2, 'k': 4, 'm': 1, 'e': 2, 'h': 1}
    >>> pool
    {'m': 1, 'q': 1}
    """
    rack_list = flatten_dict(rack)
    pool_list = flatten_dict(pool)
    
    if n < len(rack_list):
        return 
    
    while len(rack_list) != n:
        pick = random.choice(pool_list)
        rack_list.append(pick)
        pool_list.remove(pick)
        
    rack.update(count_occurrences(rack_list))
    new_pool = count_occurrences(pool_list)
    for key in list(pool):
        if key not in new_pool:
            del pool[key]
        elif pool[key] != new_pool[key]:
            pool[key] = new_pool[key]
        else:
            continue        
    
         

def compute_score(word_list, score_dic, valid_dic):
    """ (list, dict, dict) -> num
    Returns the score obtained by summing together the score of each word from word_list.
    The total score will be 0 if any of the words in word_list is not valid.
    
    >>> score_dic = {'a': 1, 'k': 3, 'p': 2}
    >>> word_list = ['aa', 'kate', 'can']
    >>> valid_dic = create_scrabble_dict(word_list)
    >>> compute_score(['kate', 'can'], score_dic, valid_dic)
    5
    
    >>> score_dic = {'a': 1, 'k': 3, 'p': 2}
    >>> word_list = ['lucky', 'cat', 'cute']
    >>> valid_dic = create_scrabble_dict(word_list)
    >>> compute_score(['hi', 'can'], score_dic, valid_dic)
    0
    
    >>> score_dic = {'a': 1, 'm': 3}
    >>> word_list = ['adorable', 'bunny']
    >>> valid_dic = create_scrabble_dict(word_list)
    >>> compute_score(['bunny'], score_dic, valid_dic)
    0
        
    """   
    score = 0
    for s in word_list:
        if (is_valid_word(s, valid_dic)):
            print 
            score += get_word_score(s, score_dic)
        else:
            return 0
    return score



def place_tiles(board, letters, row, col, direction_str):
    """ (list, str, int, int, str) -> list
    Returns a list of words created by adding those letters to the board.
    This list will contain the main word and any hook word generated. 
    
    >>> board = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], \
    [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
    >>> place_tiles(board, 'love', 0, 0, 'right')
    ['love']
    >>> display_board(board)
        0   1   2   3  
      +---------------+
    0 | l | o | v | e |
      +---------------+
    1 |   |   |   |   |
      +---------------+
    2 |   |   |   |   |
      +---------------+
    3 |   |   |   |   |
      +---------------+
    4 |   |   |   |   |
      +---------------+


    >>> board = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], \
    [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
    >>> place_tiles(board, 'rain', 1, 2, 'down')
    ['rain']
    >>> display_board(board)
        0   1   2   3  
      +---------------+
    0 |   |   |   |   |
      +---------------+
    1 |   |   | r |   |
      +---------------+
    2 |   |   | a |   |
      +---------------+
    3 |   |   | i |   |
      +---------------+
    4 |   |   | n |   |
      +---------------+
      

    >>> board = [['l', 'o', 'v', 'e'], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], \
    [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
    >>> place_tiles(board, 'et', 1, 2, 'down')
    ['vet']
    >>> display_board(board)
        0   1   2   3  
      +---------------+
    0 | l | o | v | e |
      +---------------+
    1 |   |   | e |   |
      +---------------+
    2 |   |   | t |   |
      +---------------+
    3 |   |   |   |   |
      +---------------+
    4 |   |   |   |   |
      +---------------+
    """ 
    word_list = []
    l = len(letters)
    if (direction_str == "down"):
        row_temp = row
        i = 0
        while i < l:
            if (board[row_temp+i][col] == ' '):
                board[row_temp+i][col] = letters[i]
                #find new word in "right" direction
                new_word = find_word(board[row_temp+i], col)
                if (len(new_word) != 1):
                    word_list.append(new_word)
                i += 1
            else:
                row_temp += 1
                continue
        #find new word in "down" direction
        down_string = get_vertical_axis(board, col)
        word_list.append(find_word(down_string, row))

    elif (direction_str == "right"):
        col_temp = col
        temp = 0
        while temp < l:
            if (board[row][col_temp + temp] == ' '):
                board[row][col_temp + temp] = letters[temp]
                #find new word in "down" direction
                down_string = get_vertical_axis(board, col_temp + temp)
                new_word = find_word(down_string, row)
                if (len(new_word) != 1):
                    word_list.append(new_word)
                temp += 1
            else:
                col_temp += 1
                continue                
        #find new word in "right" direction
        word_list.append(find_word(board[row], col))
        
    else:
        return []
    return word_list
    

def make_a_move(board, rack, letters, row, col, direction_str):
    """ (list, dict, int, int, str) -> list
    Returns an empty list if the direction received is neither ‘down’ nor ‘right’.
    Otherwise, the function checks if there is enough space on the board to place those letters
    and the player actually have those letters on their rack.
    If so, returns a list of words created by performing the move and the letters are place on the board.
    If the letters do not fit on the board, raises an IndexError.
    If they fit, but the player does not have those letters on their rack, raises a ValueError.

    >>> board = [['s', 'a', 't', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '],\
    [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
    >>> rack = {'a': 3, 't': 2, 's' : 1, 'r' : 1, 'i' : 1, 'n' : 1}
    >>> make_a_move(board, rack, 'rain', 1, 2, 'down')
    ['train']
    >>> rack == {'a': 2, 't' : 2, 's' : 1}
    True
    >>> display_board(board)
        0   1   2   3  
      +---------------+
    0 | s | a | t |   |
      +---------------+
    1 |   |   | r |   |
      +---------------+
    2 |   |   | a |   |
      +---------------+
    3 |   |   | i |   |
      +---------------+
    4 |   |   | n |   |
      +---------------+

    >>> board = [['k', 'a', 't', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '],\
    [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
    >>> rack = {'a': 3, 't': 2, 'c' : 1, 'r' : 1, 'i' : 1, 'n' : 1}
    >>> make_a_move(board, rack, 'rain', 1, 2, 'down')
    ['train']
    >>> rack == {'a': 2, 't' : 2, 'c' : 1}
    True
    >>> display_board(board)
        0   1   2   3  
      +---------------+
    0 | k | a | t |   |
      +---------------+
    1 |   |   | r |   |
      +---------------+
    2 |   |   | a |   |
      +---------------+
    3 |   |   | i |   |
      +---------------+
    4 |   |   | n |   |
      +---------------+
    
    >>> board = [['r', 'a', 't', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '],\
    [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
    >>> rack = {'a': 3, 't': 2, 'c' : 1, 'r' : 1, 'i' : 1, 'n' : 1}
    >>> make_a_move(board, rack, 'rain', 1, 2, 'down')
    ['train']
    >>> rack == {'a': 2, 't' : 2, 'c' : 1}
    True
    >>> display_board(board)
        0   1   2   3  
      +---------------+
    0 | r | a | t |   |
      +---------------+
    1 |   |   | r |   |
      +---------------+
    2 |   |   | a |   |
      +---------------+
    3 |   |   | i |   |
      +---------------+
    4 |   |   | n |   |
      +---------------+
    
    """
    
    if (direction_str != "down" and direction_str != "right"):
        return []
    
    #if there are enough space on board
    if (direction_str == "down"):
        down_string = get_vertical_axis(board, col)
        if(fit_on_board(down_string, letters, row)):
            if (has_letters(rack, letters)):
                return place_tiles(board, letters, row, col, direction_str)
            else:
                raise ValueError ("You don't have the letters on your rack.")
        else:
            raise IndexError ("There are not enough space on board.")
    else:
        if(fit_on_board(board[row], letters, col)):
            if (has_letters(rack, letters)):
                return place_tiles(board, letters, row, col, direction_str)
            else:
                raise ValueError ("You don't have the letters on your rack.")
        else:
            raise IndexError ("There are not enough space on board.")



if __name__ == "__main__":
    doctest.testmod()
    