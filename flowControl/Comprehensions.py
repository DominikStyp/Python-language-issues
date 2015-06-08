'''
Created on 20 mar 2014

@author: Dominik


Comprehensions is basically ability of using loop statements to filling up data structures
WARNING!!! 
1) unittest.TestCase should not have any __init__ method
2) Methods names must begin with "test"

'''
import unittest
import traceback

class Comprehensions(unittest.TestCase):

    def testlistComprehensions(self):
        print "------- " + traceback.extract_stack(None, 1)[0][-2] + " -----"
        
        ### example 1
        # fills list with squares of the number
        # x**2 acts like Math.pow(x,2)
        # prints: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
        print [x**2 for x in range(10)]
        
        ### example 2
        # we can also nest for-loops and generate list of tuples
        # prints [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
        print [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
        
        ### example 3
        # using other functions to fill list
        # prints ['3.1', '3.14', '3.142', '3.1416', '3.14159']
        from math import pi
        print [str(round(pi, i)) for i in range(1, 6)]

    
    def testdictComprehensions(self):
        print "------- " + traceback.extract_stack(None, 1)[0][-2] + " -----"
        print dict((key, value) for (key, value) in {1:'a', 2:'b'}.iteritems())
        # following works from python 2.7 or 3.x
        print { i:j for i,j in {"b":"bb", "c":"cc"}.iteritems() }
        # with additional condition: if "three" not in k
        print [(k, v) for k, v 
               in { "one": 1, "two": 2, "three": 3 }.iteritems() 
               if "three" not in k]
    
    
    def testtupleComprehensions(self):
        print "------- " + traceback.extract_stack(None, 1)[0][-2] + " -----"
        print tuple(i for i in (1,2,3))
        
    
    ''' WARNING! This is generator expression NOT A TUPLE '''
    def testgeneratorComprehensions(self):
        print "------- " + traceback.extract_stack(None, 1)[0][-2] + " -----"
        mygenerator = (x*x for x in range(3))
        for i in mygenerator:
            print "first iteration: ", i
        # this doesn't work
        # you can only iterate ONCE over generator
        for i in mygenerator: # doesn't iterate here
            print "second iteration: ", i 
        
        
if __name__ == '__main__':
    unittest.main(verbosity=4)