'''
Created on 17 mar 2014

@author: Dominik
'''

# source of Python tricks
# http://stackoverflow.com/questions/101268/hidden-features-of-python


class Testing(object):
    someAttr = "hello"

class PythonTricks(object):
    '''
    classdocs
    '''


    def __init__(self, params = None):
        '''
        Constructor
        '''
    
    def s(param):
        print param
    s = staticmethod(s)
        
    ''' No specialPythonFeatures popular language can do comparison operators chaining '''
    def chainingComparisonOperators(self):
        print "-------- chainingComparisonOperators() ---------"
        for x in range(1,20):
            if 10 < x < 20:
                print "x is between 10 and 20: ", x
                
    ''' Using generators and yield '''                
    def mygen(self):
        """Yield 5 until something else is passed back via send()"""
        print "-------- mygen() ---------"
        a = 5
        while True:
            f = (yield a) #yield a and possibly get f in return
            if f is not None: 
                a = f  #store the new value
    
    ''' For-else statement is regular for loop
        after loop else is executed, 
        but if loop is broken, else isn't executed '''
    def forElseStatement(self):
        print "-------- forElseStatement() ---------"
        for i in range(0,4):
            print "i: ", i
            if i == 0:
                break # if break is executed - else will be omitted
        else: # executes after loop, but not if loop is broken
            print("i was never 0")
            
    def inPlaceValueSwapping(self):
        print "-------- inPlaceValueSwapping() ---------"
        a = 1
        b = 2
        # here implicit tuplets are used
        # this acts like (a,b) = (b,a)
        a, b = b, a
        print a, ", ", b
        
    def createClassesOnTheFly(self):
        print "-------- createClassesOnTheFly() ---------"
        # type(name, extends, instance variables)
        NewType = type("NewType", (object,), {"x": "hello"})
        print NewType().x
        ''' 
        Preceding example is same as: 
        class NewType(object):
            x = "hello"
            n = NewType()
            n.x
        '''
        
   

obj = PythonTricks()
### ex1 chaining comparison operators
obj.chainingComparisonOperators()
### ex2 generator using yield
gen = obj.mygen()
print gen.next()
print gen.send(7)
### ex3 for-else syntax
obj.forElseStatement()
### ex4 in-place value swapping
obj.inPlaceValueSwapping()
### ex5 creating classes on-the-fly
obj.createClassesOnTheFly()

## Static method call ###
PythonTricks.s("hello i'm static")

#### shows how functions are stored internally ####
class X(object):
    def xx(self, param):
        return param
print "------ internally stored method ------ "
## You can call method using __dict__
print X.__dict__['xx'](X(),"Pass param test")

### ex missing elements of dict class ##############
''' you can inherit from dict class (dictionary) 
    and use __missing__ on missing keys
    it's some sort of php __get 
'''
class missingElems(dict):
    def __missing__(self, key):
        self[key] = rv = "hola hola"
        print "whoops, key: ", key, " is missing here"
        return rv
    
print "----- missing elements ----"
miss = missingElems()
print miss["xxx"]


