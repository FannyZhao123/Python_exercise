#Name: Wenjia Liu 
#ID: 260919690

import doctest


def create_board(row, column):
    """ (int, int) -> list
   
    Returns a list of strings which has all the elements of the sublists are strings containing only
    the space character, dimensions are based on row and column.
    
    >>> create_board(2, 3)
    [[' ', ' ', ' '], [' ', ' ', ' ']]
    >>> create_board(1, 3)
    [[' ', ' ', ' ']]
    >>> create_board(2, 5)
    [[' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ']]
    
    """
     
    two_D_list = []
    if (row <= 0 or column <= 0):
        raise ValueError ("Inputs must be both positive integers.")

    else:
        for i in range (row):
            two_D_list.append([])
            for j in range (column):
                two_D_list[i].append(' ')
        return two_D_list




def display_board (two_D_list):
    """ (list) -> None
    Displays the board, one row per line.
    
    >>> two_D_list = create_board(2, 3)
    >>> display_board(two_D_list)
        0   1   2  
      +-----------+
    0 |   |   |   |
      +-----------+
    1 |   |   |   |
      +-----------+
    
    >>> two_D_list = [[' ', ' ', ' ', ' ', ' '], [' ', 'l', 'o', 'v', 'e']]
    >>> display_board(two_D_list)
        0   1   2   3   4  
      +-------------------+
    0 |   |   |   |   |   |
      +-------------------+
    1 |   | l | o | v | e |
      +-------------------+

    >>> two_D_list = [[' ', 'g', 'o', 'o', 'd'], [' ', 'l', 'u', 'c', 'k']]
    >>> display_board(two_D_list)
        0   1   2   3   4  
      +-------------------+
    0 |   | g | o | o | d |
      +-------------------+
    1 |   | l | u | c | k |
      +-------------------+
    """
    row = len(two_D_list)
    colummn = len(two_D_list[0])
    
    #print header
    header = " "
    second_line = "  +"
    for i in range (colummn):
        header += "   " + str(i)
        second_line += "----"
    header += "  "
    second_line = second_line[:-1]  #there is an extra "-" in th end need to be removed
    second_line += "+"
    print (header)
    print (second_line)
    
    #print body
    
    for i in range (row):
        body = str(i) + " |"
        for j in range (colummn):
            body += " " + str(two_D_list[i][j]) + " |"
        print (body)
        print (second_line)
        
 
 
def get_vertical_axis(two_D_list, col):
    """ (list, int) -> list

    Returns a list of strings containing all the elements from the board depending on the number of col.
    
    >>> two_D_list = [['c', 'a', 't', ' '], [' ', 'a', 'r', 't'], [' ', ' ', 'a', ' ']]
    >>> get_vertical_axis(two_D_list, 2)
    ['t', 'r', 'a']
    
    >>> two_D_list = [['c', 'a', 't', ' ']]
    >>> get_vertical_axis(two_D_list, 1)
    ['a']
    
    >>> two_D_list = [['l', 'o', 'v', ' e']]
    >>> get_vertical_axis(two_D_list, 1)
    ['o']
    
    """  
    result = []
    for i in range (len(two_D_list)):
        result += two_D_list[i][col]
    return result
    
    
def find_word(findword_list, i):
    """ (list, int) -> str
    
    Returns the string built by connecting with the sequence of consecutive strings from the list that are not the space characters.
    Returns the empty string if in position i there is a space character.
    The sequence must include the string in position i.
    
    >>> find_word([' ', 'b', 'i', 'g', ' '], 1)
    'big'
    >>> find_word([' ', 'c', 'u', 't', 'e'], 1)
    'cute'
    >>> find_word(['l', 'i', 'g', 'h', 't'], 0)
    'light'

    """
    word = ''
    if findword_list[i] == ' ':
        return word
    else:
        for a in range (len(findword_list)):
            if findword_list[a] != ' ':
                word += findword_list[a]
            else:
                if (a < i):
                    word = ''
        return word
    
    
def available_space(space_list, i):
    """ (list, int) -> num

    Returns the number of empty squares on the row/column starting from position i.
    
    >>> space_list = ['c', ' ', ' ', 'b', ' ']
    >>> available_space(space_list, 1)
    3
    
    >>> space_list = ['c', ' ', ' ', 'b', ' ', ' ']
    >>> available_space(space_list, 3)
    2
    
    >>> space_list = ['a', ' ', ' ', 'b', ' ', ' ', 'c', ' ', ' ']
    >>> available_space(space_list, 1)
    6
    
    """    
    result = 0
    if (i < 0 or i > len(space_list)):
        raise ValueError ("Int must be between 0 and length of the string.")
    
    for a in range (i, len(space_list)):
        if (space_list[a] == ' '):
            result += 1
    return result
    
    
def fit_on_board(my_list, str_letter, i):
    """ (list, str, int) -> bool

    Returns true if the square in position i is empty and if there is enough space on the board to
    fit all the characters in letters starting from position i, false otherwise. 
    
    >>> my_list = ['a', ' ', ' ', 'b', ' ']
    >>> fit_on_board(my_list, 'lucky', 1)
    False
    
    >>> my_list =  ['a', ' ', ' ', 'b', ' ', ' ', 'c', ' ', ' ']
    >>> fit_on_board(my_list, 'best', 2)
    True
    
    >>> my_list =  ['a', ' ', ' ', 'b', ' ', ' ', 'c', ' ', ' ']
    >>> fit_on_board(my_list, 'air', 4)
    True
    """     
    if (my_list[i] != ' '):
        return False
    else:
        return (available_space(my_list, i) >= len(str_letter))
 
 
if __name__ == "__main__":
    doctest.testmod()