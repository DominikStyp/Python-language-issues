'''
Created on 14 mar 2014

@author: Dominik
'''

class MethodsIssues(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    ''' Here we defined static method
        REMEMBER:
        1) static method doesn't have self argument
        2) you have to decorate this method using @staticmethod
        3) using is Java-like: {className}.{methodName}()
    '''
        
    @staticmethod
    def stMeth(param):
        print "--- Static method stMeth() ---"
        print "param: ", param   
    
    ''' Here we defined class method
        which IS NOT INSTANCE METHOD !!!
        This is like static method but used in object context
        like: {objectInstance}.{methodName} 
        And it takes class as first argument
    
    '''
    @classmethod
    def clMeth(cls, param):
        print "--- Class method stMeth() ---"
        print "class is: ", cls
        print "param: ", param
        
        
    '''
    If we want to use var-args type like in Java: String... someVar
    we can use * before argument 
    '''
    def varArgsMethod(self, *varArgs):
        print "--- varArgsMethod ---"
        for x in varArgs:
            print x
    '''
    Python also can get "dictionary typed arguments"
    '''
    def typedArgs(self, test, **typedArgs):
        print "--- typedArgs ---"
        print "test=",test," typedArgs=", typedArgs
    '''
    We can also mix var-args with typed-var-args
    '''        
    def mixedArgs(self, *varArgs, **typedArgs):
        print "--- mixedArgs ---"
        print "varArgs:", varArgs, " typedArgs:", typedArgs
        
    def invokeOtherUsingListAndDict(self):
        myList = ["Adam","Eve"]
        myDict = { "super": "ok", "fuck":"no-ok" }
        print "--- invokeOtherUsingList ---"
        self.mixedArgs(*myList, **myDict)

    ''' Global variables works like those in PHP '''
    def changeGlobalVariable(self):
        global glob1
        glob1 = 23 #redefine global
        
    ''' WARNING: Look out for mutable arguments
        In following example each call of this method will append next argument
        to the x, it won't be overwritten
    '''
    def mutableArgsWarn(self, x=[]):
        print "--- mutableArgsWarn ---"
        x.append(1)
        print x


obj = MethodsIssues()
obj.varArgsMethod("string",0.22,None)  # string 0.22 None
obj.typedArgs(test=10, xxx=33, yyy=99) # test= 10  typedArgs= {'xxx': 33, 'yyy': 99}
obj.mixedArgs(1,3,4,typed1=0,typed2=1) # varArgs: (1, 3, 4)  typedArgs: {'typed2': 1, 'typed1': 0}

MethodsIssues.stMeth("static123") # used only in "static way"
obj.clMeth("class123") # same as static but used in object context

# using method to pass var-args and typed-args to another
obj.invokeOtherUsingListAndDict() # varArgs: ('Adam', 'Eve')  typedArgs: {'super': 'ok', 'fuck': 'no-ok'}

# test if global variable works inside method
glob1 = 0
obj.changeGlobalVariable()
print "changing of global variable: ", glob1

# test of mutableArgsWarn
obj.mutableArgsWarn() # [1]
obj.mutableArgsWarn() # [1,1] - argument is not overwritten



