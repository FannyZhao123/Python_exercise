#Name: Wenjia Liu
#ID: 260919690

from crypto_helpers import * 

def caesar (in_string, k, m):
    '''
    Input: a string (the message to encrypt/decrypt), a integer k (the key of the cipher),
    and another integer m representing the mode (encrypt/decrypt).Specially, when m is 1, the function will be encrypting the message,
    if instead it is  1 the function will be decrypting the message.
    If it has any other value, the function raises a ValueError indicating that no other mode is supported.
    Return: a string obtained by encrypting or decrypting (depending on m) the message received as input using the Caesar’s cipher with key k.
    >>> caesar('soul', 6, 1)
    'yuar'

    >>> caesar('happy', 9, -1)
    'yrggp'
    
    >>> caesar('light', 10, 1)
    'vsqrd'
    
    '''
       
    result = ""
    if (m == 1):
        #encrypting the message.
        for i in range (len(in_string)):
            if (in_string[i] == " "):
                result += " "
            else:
                result += shift_char(in_string[i], k)
        return result

    elif (m == -1):
        #decrypting the message.
        for i in range (len(in_string)):
            if (in_string[i] == " "):
                result += " "
            else:
                result += shift_char(in_string[i], -k)
        return result 
    else:
        raise ValueError("mode not supported.")



def vigenere (in_string, key, m):
    '''
    Input: a string representing the message to encrypt/decrypt, another string representing the key of the cipher, and an integer m representing the mode (encrypt or decrypt). 
    Specially, when m is 1, the function will be encrypting the message, if instead it is  1 the function will be decrypting the message.
    If it has any other value, the function raises a ValueError indicating that no other mode is supported.
    Then the function will return a string obtained by encrypting or decrypting (depending on m) the message received as input using the Vigen`ere’s cipher with key received as input.
    Besides, the function will raise an error if the string representing the key is empty.
    >>> vigenere('coke', 'light', 1)
    'nwql'
    
    >>> vigenere('banana', 'grass', 5)
    Traceback (most recent call last):
    ValueError: mode not supported

    >>> vigenere('love', 'soul', -1)
    'tabt'

    ''' 
           
    if (not (in_engl_alpha(key))) :
        raise ValueError("The key should not be empty and only has english chara in it ")
    
    key = pad_keyword (key, len(in_string))
    k = get_keys(key)
    result = ""
    
    if (m == 1):
        #encrypting the message.
        for i in range(len(k)):
            if (in_string[i] == " "):
                result += " "
            else:
                result += shift_char(in_string[i], k[i])
                #in_string[i] -- the i-th elements in in_string
                #k[i] --- the i-th element in k
                #shift_char -- shift the char to next k[i] th place
        return result
    
    elif (m == -1):
        #decrypting the message.
        for i in range(len(k)):
            if (in_string[i] == " "):
                result += " "
            else:
                result += shift_char(in_string[i], -k[i])
        return result
    
    else:
        raise ValueError("mode not supported.")

