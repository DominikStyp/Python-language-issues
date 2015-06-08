'''
Created on 15 mar 2014

@author: Dominik
'''

class SpecialMethods(object):
    '''
    classdocs
    '''

    # Constructor is called when instance is created
    def __init__(self):
        print "__init__"
        
    # Is called to create new instance of class
    # Use __new__ when you need to control the creation of a new instance
    # You shouldn't need to override __new__ 
    #  unless you're subclassing an immutable type like str, int, unicode or tuple
    # But in most cases you don't need this - use __init__ instead
    def __new__(cls):
        print "__new__"
        return super(SpecialMethods, cls).__new__(cls)
    
    # Destructor is called when object instance is about to destroy
    # !!!IMPORTANT!!! this won't be invoked while there is any reference to the object
    def __del__(self):
        print "__del__"    
        
    # Defines string representation of the object (USE IT FOR DEBUGGING)
    # This should be representation of python object usually eval will convert it back to that object
    def __repr__(self):
        return "---------Representation of SpecialMethods"
    
    # Defines Java-like .toString() method, which is invoked when string representation is used
    # for normal purposes
    def __str__(self):
        return "---------I'm SpecialMethods"
    
    # Invoked when you try to get non-existent attribute
    def __getattr__(self, name):
        print "you tried to get nonexistent attribute!"
        return False
    
    # Invoked when you try to call object as function
    def __call__(self, *args):
        print "You called me with args: ", args


        
#### example 1 ###
print "---------------- example 1 -  __del__  ------------"
obj = SpecialMethods()
print "assign obj = None"
obj = None # here we destroy object


#### example 2 - __del__ won't be invoked, because 1 reference still remains ####
print "---------------- example 2 -  __del__ won't be invoked ------------"
obj1 = SpecialMethods()
obj1ref1 = obj1
obj1 = None
# __del__ will be invoked at the end of script, where everything is destroyed ###

print "---------------- example 3 - __str__ vs __repr__ ------------"
obj = SpecialMethods()
print obj # __str__ will be invoked
# difference example
import datetime
today = datetime.datetime.now()
print "__str__ should be: ", str(today)
print "__repr__ should be: ", repr(today)
obj = None

print "---------------- example 4 __getattr__ getting non-existent attribute"
obj = SpecialMethods()
print obj.nonexistent

print "---------------- example 5 __call__ while calling object as function "
obj = SpecialMethods()
print obj("arg1","arg2")



print "end of script"