'''
Created on 17 mar 2014

@author: Dominik
'''

class Sets(object):
    '''
    classdocs
    '''


    def __init__(self, params=None):
        '''
        Constructor
        '''
    '''
     Set is something like list with unique elements
    '''
    def usingSets(self):
        print "------- usingSets() -------"
        print set(['a','b','c','a']) # set(['a', 'c', 'b'])
        # WARNING! Letters won't be ordered this way
        print set('Brian') # set(['i', 'a', 'r', 'B', 'n'])
    
    def operationsBetweenSets(self):
        print "------- operationsBetweenSets() -------"
        a = set(['a','b','c','d','e'])
        b = set(['c','d','e','f','g'])
        # a elements AND NOT b elements
        print a - b # set(['a', 'b'])
        # a elements AND b elements (common elements)
        print a & b # set(['c', 'e', 'd'])
        # a elements XOR b elements (without common elements)
        print a ^ b # set(['a', 'b', 'g', 'f'])
        # a elements OR b elements (sum a+b)
        print a | b # set(['a', 'c', 'b', 'e', 'd', 'g', 'f'])
        
    def checkSubsets(self):
        print "------- checkSubsets() -------"
        # is set([]) subset of set([]):
        print set([1,2,3,4]).issubset([0,1,2,3,4,5]) # true
        
        
#### 
Sets().usingSets()
Sets().operationsBetweenSets()