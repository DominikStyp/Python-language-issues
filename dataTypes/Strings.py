'''
Created on 14 mar 2014

@author: Dominik
'''



class Strings(object):
    '''
    classdocs
    '''

    def toString(self, s):
        return str(s)

    def __init__(self):
        '''
        Constructor
        '''
        
    ''' 
    Watch out!!! Here we've overridden str() funcion by local variable str
    In this case we need to use defined toString() 
    '''    
    def checkings(self):
        print '----- checkings() ----- '
        strV = "some string to test"
        print "isdigit:" + self.toString(strV.isdigit())
        print "islower:" + self.toString(strV.islower())
        print "isupper:" + self.toString(strV.isupper())
        print "isalpha:" + self.toString(strV.isalpha())
        print "starts with: " + self.toString(strV.startswith("some")) 
        print "string has substring: " + str(strV.find("to"))
        print "string hasn't substring: " + str(strV.find("xxx"))
        print "count substring: " + self.toString(strV.count("t"))
        
    def modifications(self, s):
        import string
        print '----- modifications() ----- '
        print "capitalize: " + s.capitalize()
        print "capitalize words: " + string.capwords(s, None)
        print "replace: " + string.replace(s, 'test', '123')
        
    def substringMethods(self):
        print '----- substringMethods() ----- '
        testS = "some@kind-of!test#string*123456"
        print "ALL STRING: \t\t\t", testS
        # we can treat string as list and printing characters as list elements
        print "chars 1-3:\t\t\t", testS[1:3]
        print "-3 char (off the end):\t\t", testS[-3]
        print "last 3 chars:\t\t\t", testS[-3::]
        print "from 0 to -3:\t\t\t", testS[:-3]
        print "step iteration, every step +2: ", testS[::2]
        print "ALL REVERSED:\t\t\t", testS[::-1]
        print "reversed, -11 to end:\t\t", testS[11::-1]
        print "reversed, -11 to -7:\t\t", testS[11:7:-1]
        
    def formatting(self):
        print '----- formatting() ----- '
        print 'Hello {username}! Your birthdate is {birthdate}'.format(username="John", birthdate='25-11-2010')
        print 'List some vars: {0}, {1}, {2}'.format("one","two","three")
        print '12'.zfill(5) #zero fill
        # using dictionary argument to format
        table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
        print 'Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table)
        
    # watch out for common errors that can occur inside methods
    def commonErrors(self, str):
        ##### OVERRIDE str() function ##################################
        # if you define param str, you overwrite str() global method
        ## print str(1) # so you can't now use str()
        # but you can do following, and instead using str() use toString()
        from __builtin__ import str as toString
        print toString(1)
        
        

obj = Strings()
obj.checkings()
obj.modifications("some test string to change")
obj.formatting();
obj.substringMethods()
obj.commonErrors("xxx")