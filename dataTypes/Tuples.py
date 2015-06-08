'''
Created on 14 mar 2014

@author: Dominik

Tuple = Krotki [PL]

IMPORTANT!!
Tuple are immutable, you can't change elements after tuple declaration


'''

class Tuples(object):
    '''
    classdocs
    '''
    def __init__(self, params):
        '''
        Constructor
        '''
    # REMEMBER! Tuple always has comma inside declaration, even if it has 1 element
    def declaration(self):
        print "--- declaration() ---" 
        tup1 = 'hello1', # comma is obligatory, otherwise it will be string
        tup2 = ('hello2') # WARNING! This is string, no comma inside!
        tup3 = ()
        tup4 = ('hello4','hello44')
        # <type 'tuple'> <type 'str'> <type 'tuple'> <type 'tuple'>
        print type(tup1), type(tup2), type(tup3), type(tup4)
        
        
        
    def simpleTuple(self):
        print "--- simpleTuple() ---"
        simpleTuple = (1,'ok',3.33)
        for x in simpleTuple: 
            print "tuple elem: ", x;
            
        
    ''' IMPORTANT!!
        This works EXACTLY THE SAME FOR LISTS
    '''
    def slicingTuple(self):
        print "------- slicingTuple() -------"
        testS = ("one", "two", 3, 4, "5-five", "6-six")
        print testS
        print "elements 1-2:\t\t\t", testS[1:3] # last is exlusive
        print "-3 element (off end):\t\t", testS[-3]
        print "last 3 elements:\t\t", testS[-3::]
        print "from 0 to -3:\t\t\t", testS[:-3]
        print "step iteration, every step +2: ", testS[::2]
        print "reversed :\t\t", testS[::-1]
        print "reversed, -4 to end:\t\t", testS[4::-1]
        print "reversed, -4 to +2 reversed:\t\t", testS[4:2:-1]
        
    def usingTupleToReplaceVars(self):
        print "--- usingTupleToReplaceVars() ---"
        a = 5
        b = 10
        print "a:", a, "b:", b
        a,b = b,a # here implicit tuple is used
        print "a:", a, "b:", b
        
    def tuplesAreImmutable(self):
        print "--- tuplesAreImmutable() ---"
        testTup = (3,4,5,6)
        '''
            estTup[2] = 10
            TypeError: 'tuple' object does not support item assignment
        '''
        testTup[2] = 10 # can't change tuple element
        print testTup
    
    ''' Great is dynamically assigning tuple elements to variables '''
    def assigningToVarsDynamically(self):
        print "--- assigningToVarsDynamically() ---"
        testTup = ("Kate", 1, 3.33, None)
        strVar, intVar, floatVar, noneVar =  testTup
        print strVar, intVar, floatVar, noneVar
        


obj = Tuples(0)
# obj.simpleTuple()
obj.slicingTuple()
# obj.usingTupleToReplaceVars()
# obj.tuplesAreImmutable()
# obj.assigningToVarsDynamically()
# obj.declaration()
        