class Cake:
    
    # constructor
    def __init__ (self, n, i):
        self.name = n
        if (len(i) < 3):
            raise ValueError ("A cake must contain at least three or more ingredients.")
        self.ingreds = i
        self.price = 10 + 5*random.random()
    
    def __str__ (self):
        """ (Cake) -> str
        Returns a string containing the name of the cake and its price.
        
        >>> self = Cake('walnut cake', ['i', 'j', 'c'])
        >>> Cake. __str__ (self)
        'walnut cake $12.34'
        
        >>> self = Cake('pink cake', ['a', 'b', 'c'])
        >>> Cake. __str__ (self)
        'pink cake $10.79'
        
        >>> self = Cake('banana cake', ['i', 'c', 'r'])
        >>> Cake. __str__ (self)
        'banana cake $11.76'       
        """
        p = self.price
        result = self.name + ' $' + str(round(p, 2))
        return result
    
    def is_better (self, other):
        """ (Cake) -> bool
        Returns true if the current one has a better (lower) ratio between price and number of ingredients,
        false otherwise.
        
        >>> self = Cake('apple cake', ['a', 'b', 'c', 'd'])
        >>> other = Cake('banana cake', ['i', 'j', 'k'])
        >>> Cake.is_better(self, other)
        True
        
        >>> self = Cake('pink cake', ['a', 'b', 'c'])
        >>> other = Cake('walnut cake', ['i', 'd', 'k'])
        >>> Cake.is_better(self, other)
        False
        
        >>> self = Cake('redvelvet cake', ['a', 'b', 'c'])
        >>> other = Cake('lemon cake', ['s', 'i', 's'])
        >>> Cake.is_better(self, other)
        False        
        """
        p1 = self.price/len(self.ingreds)
        p2 = other.price/len(other.ingreds)
        if (p1 < p2):
            return True
        else:
            return False

def create_menu (dic):
    """ (dict) -> Cake
    Return a list of Cake objects.
    Display the menu as well, one cake per line.
    
    >>> dic = {'A': ['a', 'd', 'f'], 'B': ['a', 'b', 'c', 'g'], 'C':['b', 'c', 'l', 'k', 'p', 'u']}
    >>> a = create_menu (dic)
    A $12.6
    B $12.75
    C $10.02
    
    >>> dic = {'a': ['c', 'r', 'm'], 'r': ['v', 'h', 'k'], 'C':['p', 'p', 'r', 'k', 'p', 'u']}
    >>> a = create_menu (dic)
    a $12.71
    r $14.09
    C $11.69
        
    >>> dic = {'i': ['s', 'i', 'y'], 'j': ['s', 'h', 'k'], 'k':['s', 'e', 'r', 'e']}
    >>> a = create_menu (dic)
    i $11.23
    j $10.56
    k $10.18
    """
    cakes = []
    for key in dic:
        cakes.append(Cake(key, dic[key]))
    for i in cakes:
        print (i)
    return cakes
    
    
def find_best (cakes):
    """ (list) -> Cake
    Returns the best cake in the list.

    >>> cakes = [Cake('apple cake', ['a', 'b', 'c']), Cake('banana cake', ['a', 'b', 'l', 'c']), Cake('pear cake', ['a', 'b', 'c', 'k', 'o'])]
    >>> b = find_best (cakes)
    >>> print (b)
    pear cake $14.74
    
    >>> cakes = [Cake('lemon cake', ['k', 'p', 'y']), Cake('blueberry cake', ['l', 'x', 'm', 'n']), Cake('pink cake', ['c', 'b', 'c', 'k', 'o'])]
    >>> b = find_best (cakes)
    >>> print(b)
    pink cake $12.96
    
    >>> cakes = [Cake('chocolate cake', ['c', 's', 't']), Cake('strawberry cake', ['s', 'a', 't', 'b']), Cake('carrot cake', ['i', 'b', 'a'])]
    >>> b = find_best(cakes)
    >>> print(b)
    strawberry cake $11.67        
    """
    best = cakes[0]
    for i in range (1, len(cakes)):
        if (cakes[i].is_better(best)):
            best = cakes[i]
        else:
            continue
    return best
    
    
