'''
Created on 15 mar 2014

@author: Dominik
'''

class ComparableObjects(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    # x < y => x.__lt__(y)
    def __lt__(self, other):
        print "__lt__"
        return False
    # x <= y => x.__le__(y)
    def __le__(self, other):
        print "__le__"
        return False
    # x == y => x.__eq__(y)
    def __eq__(self, other):
        print "__eq__"
        return False
    # x != y => x.__ne__(y)
    def __ne__(self, other):
        print "__ne__"
        return False
    # x > y => x.__gt__(y)
    def __gt__(self, other):
        print "__gt__"
        return False
    # x >= y => x.__ge__(y)
    def __ge__(self, other):
        print "__ge__"
        return False
    
## Comparable object example
obj0 = ComparableObjects()
obj1 = ComparableObjects()

if obj0 == 1: # here  obj0.__eq__(1) is invoked
    print "this is 1"
else:
    print "not 1"

        
        
        