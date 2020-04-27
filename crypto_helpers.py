#Name:Wenjia Liu
#ID: 260919690


ALPHABET = 'abcdefghijklmnopqrstuvwxyz'


def in_engl_alpha(s):
    '''
    Input: a string -- the string we want to decide if it only has english alpha
    Return: 1. true,  when it's not empty and only has english chara in it
            2. false,  otherwise
   
    >>> in_engl_alpha (' ')
    False
        
    >>> in_engl_alpha ('@')
    False
        
    >>> in_engl_alpha ('WWW')
    True
    
    '''
  
    if not s:
        #s is empty string 
        return False 
    elif not s.isalpha():
        # s is.alpha() will return: True, when s only has english;
        #                          False, when s has other char other than english.
    
        return False
    else:
        return True



def shift_char(input_char, n):
    '''
    Input: a string representing a character, and an int n
    Generally, the function returns the lower case letter which appears n position later in the alphabet.
    Specially, the function returns the character itself with no modification, if the character received as input is not a letter of the English alphabet.
    >>> shift_char('a', 86)
    'i'
    
    >>> shift_char('b',99)
    'w'
    
    >>> shift_char('j', 66)
    'x'
     
    '''
   
   
    if (len(input_char) != 1):
        raise ValueError ("the input string should contain a single character.")
    elif not input_char.isalpha():
        return input_char
    else:
        input_char = input_char.lower()
        new_position = (ALPHABET.find(input_char) + n) % 26
        new_letter = ALPHABET[new_position]
        return new_letter



def get_keys(input_string):
    '''
    Input: a string 
    Return: a list of integers
    Raise error when it contains not only the chars
    >>> get_keys('love')
    [11, 14, 21, 4]
    
    >>> get_keys('phd')
    [15, 7, 3]
    
    >>> get_keys('wind')
    [22, 8, 13, 3]

    '''
    
    int_list = []
    if not input_string:
        return int_list
    elif not input_string.isalpha():
        raise ValueError ("the input string must contain only characters from the English alphabet.")
    else:
        input_string = input_string.lower()
        for i in range(len(input_string)):
            int_list.append(ALPHABET.index(input_string[i]))
        return int_list


def pad_keyword(s, n):
    '''
    Input: a string and an integer n.
    Return: a string of length n
    If the input string is empty, the function raise a ValueError with the appropriate message.
    >>> pad_keyword('apple', 10)
    'appleapple'
    
    >>> pad_keyword('love', 2)
    'lo'
    
    >>> pad_keyword('toy', 4)
    'toyt'
    
    '''
    
    if not s:
        raise ValueError ("the input string can not be empty.")
    result = ""
    for i in range (n):
        result += (s[i%len(s)])
    return result

