'''
Created on 14 mar 2014

@author: Dominik

Important!!!
Dictionaries in Python are HashMap counterpart from Java
or associative array from PHP
'''

class Dictionaries(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
    def dictExample(self):
        simpleDict = { "orange": "fruit", 
                       "cucumber": "vegetable",
                       "lamb": "meat" 
                     }
        # update by dictionary syntax
        simpleDict.update({ "orange": "citrus fruit" })
        # update by var syntax
        simpleDict.update( lamb="red meat" )
        # loop over elements
        for key,val in simpleDict.items():
            print key, " is ", val
        # get sigle value by key
        print simpleDict.get("lamb") # red meat
        print simpleDict['lamb'] # red meat
        # delete key
        del simpleDict['lamb']
        print simpleDict # {'orange': 'citrus fruit', 'cucumber': 'vegetable'}
        # clear dictionary
        simpleDict.clear()
        
    # You don't necessary need to quote around every dictionary argument
    # Examples in following method
    def betterSyntax(self):
        d = dict(a=10, bbb=32, someBiggerVar="lol") # by **kwargs syntax is allowed
        # but you can't use this like below, 
        # because in following Python will look for "a", and "bigV" vars
        # d2 = {a:10, bigV:11}
        print d
        
        
    ''' To prevent exceptions getting non-existent elements
        you can use get() with default argument '''
    def dictionaryGet(self):
        print "------ dictionaryGet() ------"
        d1 = {"a": 1, "b": 2, "c": 3}
        # causes exception KeyError: 'd' 
        #    print d1["d"]
        # but this will print default value
        print d1.get("d",0) # prints 0
        print d1.get("a",0) # prints 1 because "a" exists
        
        

obj = Dictionaries(0)
obj.dictExample()
obj.betterSyntax()
obj.dictionaryGet();