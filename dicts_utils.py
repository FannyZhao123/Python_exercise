#Name: Wenjia Liu 
#ID: 260919690

import doctest

def count_occurrences(word):
    """ (str) -> dict

    Returns a dictionary mapping characters to integers.
    The keys in the dictionary are the characters from word.
    the values represent the number of occurrences of those characters in the word. 
    
    >>> count_occurrences('apple')
    {'a': 1, 'p': 2, 'l': 1, 'e': 1}
    >>> count_occurrences('love')
    {'l': 1, 'o': 1, 'v': 1, 'e': 1}
    >>> count_occurrences('lucky')
    {'l': 1, 'u': 1, 'c': 1, 'k': 1, 'y': 1}

    """ 
    d = {}
    for i in word:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    return d


def flatten_dict (dic):
    """ (dict) -> list
   
    Returns a list containing the keys in the dictionary.
    Each key appears in the list as many times as the value associated to such key.

    >>> dic = {'a' : 1, 'f' : 1, 'k' : 1}
    >>> flatten_dict(dic)
    ['a', 'f', 'k']

    >>> dic = {'cat': 2, 'dog': 0}
    >>> flatten_dict(dic)
    ['cat', 'cat']
    
    >>> dic = {'bunny': 2, 'cute': 1}
    >>> flatten_dict(dic)
    ['bunny', 'bunny', 'cute']
    
    """      
    result = []
    for key in dic:
        for i in range (dic[key]):
            result.append(key)
    return result
    

def get_word_score(getword_str, dic):
    """ (str, dict) -> int
    Returns the score of getword_str computed by summing together the value of each character in getword_str.
    
    >>> dic = {'a': 2, 'b': 1, 'n': 2}
    >>> get_word_score('bunny', dic)
    5

    >>> dic = {'a': 2, 'b': 0, 'e': 2}
    >>> get_word_score('apple', dic)
    4
    
    >>> dic = {'a': 2, 'b': 0, 'r': 1}
    >>> get_word_score('admire', dic)
    3
    """ 
    score = 0
    for i in getword_str:
        if i in dic:
            score += dic[i]
        else:
            score += 0
    return score
  

def is_subset(first_dict, second_dict):
    """ (dict, dict) -> bool
    Returns true if first_dict can be considered to be a subset of second_dict.
    
    >>> first_dict = {'a': 2, 'c': 1}
    >>> second_dict = {'a': 2, 'b': 1}
    >>> is_subset(first_dict, second_dict)
    False

    >>> first_dict = {'c': 1}
    >>> second_dict = {'a': 2, 'c': 1}
    >>> is_subset(first_dict, second_dict)
    True

    >>> first_dict = {'c': 1}
    >>> second_dict = {'a': 2, 'b': 1, 'c': 2}
    >>> is_subset(first_dict, second_dict)
    True
    
    """
    result = True
    for key in first_dict:
        if key in second_dict:
            if first_dict[key] <= second_dict[key]:
                continue
            else:
                return False
        else:
            return False
    return result


def subtract_dicts(d1, d2):
    """ (dict, dict) -> bool
    
    Returns the updated d1 by replacing the values associated to the common keys with
    the difference between the original value in d1 and the value in d2, if If d2 is a subset of d1. Otherwise, d1 remains as is. 
    Returns true if d2 was a subset of d1, false otherwise.

    >>> d1 = {'a': 2, 'b': 1, 'c': 2}
    >>> d2 = {'a': 1, 'b': 5, 'c': 3}
    >>> subtract_dicts(d1, d2)
    False
    >>> d1 == {'a': 2, 'b': 1, 'c': 2}
    True


    >>> d1 = {'a': 2, 'b': 1, 'c': 2}
    >>> d2 = {'a': 2, 'c': 1}
    >>> subtract_dicts(d2, d1)
    False
    >>> d2 == {'a': 2, 'c': 1}
    True

    >>> d1 = {'c': 1}
    >>> d2 = {'a': 2, 'b': 1, 'c': 2}
    >>> subtract_dicts(d2, d1)
    True
    >>> d2 == {'a': 2, 'b': 1, 'c': 1}
    True
    
    """
    result = is_subset (d2, d1)
    
    if result:
        for key in d2:
            d1[key] -= d2[key]
            
    for k in list(d1):
        if d1[k] == 0:
            del d1[k]
    
    return result


def create_scrabble_dict(create_scrabble_list):
    """ (list) -> dict
    Returns a dictionary that maps integers representing the number of characters in a word to a dictionary of words with the specified length.
    The latter maps a single letter to a list of words beginning with such letter.
    
    >>> create_scrabble_list = ['aa', 'qi', 'za']
    >>> create_scrabble_dict(create_scrabble_list)
    {2: {'a': ['aa'], 'q': ['qi'], 'z': ['za']}}
    
    >>> create_scrabble_list = ['good', 'luck']
    >>> create_scrabble_dict(create_scrabble_list)
    {4: {'g': ['good'], 'l': ['luck']}}
    
    >>> create_scrabble_list = ['ac', 'd']
    >>> create_scrabble_dict(create_scrabble_list)
    {2: {'a': ['ac']}, 1: {'d': ['d']}}
    
    """
    #return a dic of dic
    d = {}
    for i in create_scrabble_list:
        if len(i) in d:
            temp1 = d[len(i)]
            
            if i[0] in temp1:
                temp1[i[0]].append(i)
            else:
                temp1[i[0]] = i.split()
                
            d[len(i)] = temp1
            
        else:
            temp2 = {}
            temp2[i[0]] = i.split()
            d[len(i)] = temp2
    return d


def is_valid_word(valid_str, dic):
    """ (str, dict) -> bool
    Returns true if the input string appears in the dictionary, false otherwise.
    
    >>> valid_str = ['aa', 'qi', 'za']
    >>> dic = create_scrabble_dict(valid_str)
    >>> is_valid_word('aa', dic)
    True
    
    >>> valid_str = ['aa', 'ki', 'zz']
    >>> dic = create_scrabble_dict(valid_str)
    >>> is_valid_word('cc', dic)
    False
    
    >>> valid_str = ['cc', 'kk']
    >>> dic = create_scrabble_dict(valid_str)
    >>> is_valid_word('kk', dic)
    True
    
    """    
    if len(valid_str) in dic:
        inner_dic = dic[len(valid_str)]
        if valid_str[0] in inner_dic:
            if valid_str in inner_dic[valid_str[0]]:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
 
 
if __name__ == "__main__":
    doctest.testmod()