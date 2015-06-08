'''
Created on 14 mar 2014

@author: Dominik
'''

class A(object):
    '''
    classdocs
    '''
    aString = "String in A"
    name = "I'm A"
    # following will be renamed into _A__renamedVar in B class, this is overwrite protection
    # if you prepend var name with __ automatic rename will occur
    __renamedVar = " renamedVar "
    def __init__(self):
        '''
        Constructor
        '''
'''
    classdocs
    B(A) means that B inherits from A
'''
class B(A):
    name = "I'm B"
    # REMEBER __init__ doesn't invoke __init__ from parent class (like in Java)
    # You have to do this by yourself
    '''
        Constructor
    '''
    def __init__(self):
        A.__init__(self) # invoke constructor from parent
        # specialPythonFeatures way to invoke constructor, without using A class name
        # super(B,self).__init__() 
        
    def printName(self):
        print "B: ", self.name  # accessing instance variables
        print "A: ", A.name     # you can access parent instance vars via class name
        
        
obj = B()
obj.printName()
## some magic has happened and __renamedVar became _A__renamedVar just for protection of overwrite 
print obj._A__renamedVar

