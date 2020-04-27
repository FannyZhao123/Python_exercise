def get_triangle(n, s):
    """ (int, str) -> str
    Returns a string representing a triangle where n is one of
    the triangle’s heights and s is the symbol used to draw it.
    Returns an empty string if the input provided is 0.
    Raises ValueError if the provided integer is a negative number
    or the provided input string does not contain at least one character. 
    
    >>> get_triangle(0, 'a')
    ''
    
    >>> a = get_triangle(6, 'A')
    >>> print(a)
    A 
    A A 
    A A A 
    A A A A 
    A A A A A 
    A A A A A A 
    A A A A A 
    A A A A 
    A A A 
    A A 
    A 

    >>> a = get_triangle(8, '')
    Traceback (most recent call last):
    ValueError:  Provided integer cannot be negetive, and the string need to contain at least 1 char. 
        
    """

    result  = ''
    if (n < 0 or s == ''):
        raise ValueError (" Provided integer cannot be negetive, and the string need to contain at least 1 char. ")
    elif ( n == 0 ):
        return result
    else:
        for i in range (1, n+1):
            for j in range (1, i+1):
                result += s 
                result += ' '
            result += '\n'
        while (n > 0):
            for i in range (1, n):
                result += s 
                result += ' '
            if (n >= 3):
                result += '\n'
            n -= 1
        return result     