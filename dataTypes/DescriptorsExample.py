'''
Created on 19 mar 2014

@author: Dominik

Here we have practical example of how to use Descriptors
Main issues:
- Descriptors can act as properties, 
    if you set property __set__ will be invoked
    if you get property __get__ will be invoked 
- Descriptors MUST be defined at the class level,
  if you define descriptor like: self.title = NonNegative(0)
  inside a method - it won't work properly
'''

# http://nbviewer.ipython.org/urls/gist.github.com/ChrisBeaumont/5758381/raw/descriptor_writeup.ipynb

''' WARNING!! Following descriptor is WRONG!
    That's because it doesn't use instance argument,
    hence every instance will have same value, which is bad
'''
class BadNonNegative(object):
    def __init__(self, default):
        self.value = default
        
    def __get__(self, instance, owner):
        return self.value
    
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Negative value not allowed: %s" % value)
        self.value = value



''' This is good descriptor, because it uses instance argument
    to recognize which instance is considered here '''
from weakref import WeakKeyDictionary   
class NonNegative(object):
    """A descriptor that forbids negative values"""
    def __init__(self, default):
        self.default = default
        self.data = WeakKeyDictionary()
        
    def __get__(self, instance, owner):
        # we get here when someone calls x.d, and d is a NonNegative instance
        # instance = x
        # owner = type(x)
        return self.data.get(instance, self.default)
    
    def __set__(self, instance, value):
        # we get here when someone calls x.d = val, and d is a NonNegative instance
        # instance = x
        # value = val
        if value < 0:
            raise ValueError("Negative value not allowed: %s" % value)
        self.data[instance] = value

        
class Movie(object):
    
    #always put descriptors at the class-level
    rating = NonNegative(0)
    runtime = NonNegative(0)
    budget = NonNegative(0)
    gross = NonNegative(0)
    
    def __init__(self, title, rating, runtime, budget, gross):
        self.title = title
        self.rating = rating
        self.runtime = runtime
        self.budget = budget
        self.gross = gross
    
    def profit(self):
        return self.gross - self.budget
    
    
m = Movie('Casablanca', 97, 102, 964000, 1300000)
print m.budget  # calls Movie.budget.__get__(m, Movie)
m.rating = 100  # calls Movie.budget.__set__(m, 100)
try:
    m.rating = -1   # calls Movie.budget.__set__(m, -100)
except ValueError:
    print "Woops, negative value"