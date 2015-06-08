'''
Created on 14 mar 2014

@author: Dominik
'''


class LoopTypes(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''

    def simpleFor(self):
        print("---- simpleFor ----")
        for i in range(1,3):
            print "simple for " + str(i)
            
    def simpleForOverStringChars(self):
        print("---- simpleForOverStringChars ----")
        for chr in "abcdef":
            print chr
             
            
    ''' WARNING!! There's no ++/-- operator in Python '''
    def simpleWhile(self):
        print("---- simpleWhile ----")
        x = 0
        while x < 10:
            x += 1
            if x == 3: break
            print "x = " + str(x)
    '''  
    We can use enumerate instead of Java's for(int i=0; i<arr.lenght; i++){}
    enumerate object can be accessed like array via index
    each 'el' is enumerate object
    '''      
    def usingEnumerate(self):
        print("---- usingEnumerate ----")
        simpleArr = ['one', 'two', 'three', 'four']
        for el in enumerate(simpleArr):
            print "element num: ", el[0] , " element val: " + el[1];
        # foreach-like
        for num,val in enumerate(simpleArr):
            print "num:", num, " value: ", val
    
    ''' zip() combines lists into tuples for each element of every list
        1) You can combine many lists/tuples
        2) if lists/tuples are not symmetric, 
           number of displayed elements will be of the smaller list/tuple size  
    '''
    def usingZip(self):
        print("---- usingZip ----")
        a = ['a','b','c', 'd',  'e']
        b = [11,12,13]
        c = ("aChar", "bChar", "cChar", "dChar")
        # this will print 3 pairs because b is smaller list
        for aVal, bVal, cVal in zip(a,b,c):
            print aVal, " => ", bVal, " => ", cVal # a  =>  11  =>  aChar ...
            
    ''' sorted() function allows you to sort sets in their natural order 
        1) None goes before every specialPythonFeatures type
        2) Integers
        3) Capital strings
        4) Regular strings
    '''
    def usingSortedSet(self):
        print("---- usingSortedSet ----")
        s = set(['bad', 'Alice', 'apple', 1, 2, None, "_three"])
        # prints: None, 1, 2, Alice, _three, apple, bad
        for el in sorted(s):
            print el
            
    ''' itering over dictionary goes like foreach loop in PHP ''' 
    def loopOverDictionary(self):
        print("---- loopOverDictionary ----")
        dict1 = { 'a': 1, 'b': 2, "c": 10, 'd': 22 }
       
        ### simple loop
        print "--- .iteritems() ---"
        for k,v in dict1.iteritems():
            print k, " => ", v
        
        ### list all items to variables in one step
        print "--- use itemgetter() from operator ---"
        from operator import itemgetter
        a,b,c,d = itemgetter('a','b','c','d')(dict1)
        print "vars in one step (way 1): ", a, " ", b, " ", c, " ", d
        
        ### all items in one step... specialPythonFeatures way
        a,b,c,d = (dict1[i] for i in ('a', 'b', 'c', 'd'))
        print "vars in one step (way 2): ", a, " ", b, " ", c, " ", d
    
    
    ''' if you need defined step inside your loop you can use xrange '''
    def usingXrange(self):
        print("---- usingXrange ----")
        # prints: 1  4  7  10  13  16  19
        # xrange(from, to, step)
        for i in xrange(1,20,3):
            print i
            
    def measuringExecutionTimes(self):
        print "---- measuringExecutionTimes() ----"
        def f(x):
            return x * x
        import timeit
        print timeit.repeat("for x in range(100): lambda x: x*10","",
                  number=100000)
        


obj = LoopTypes()
obj.simpleFor()
obj.simpleForOverStringChars()
obj.simpleWhile()
obj.usingEnumerate()
obj.usingZip()
obj.usingSortedSet()
obj.loopOverDictionary()
obj.usingXrange()
obj.measuringExecutionTimes()
