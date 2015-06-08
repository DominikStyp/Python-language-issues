'''
Created on 28 mar 2014

@author: Dominik
'''

class Test1(object):
    
    def meth1(self):
        print "Test1.meth1()"
    def meth2(self):
        print "Test1.meth2()"
        

# You can overwrite methods from the same class
# But look out for for mixing methods from different classes,
# because Python will complain about SELF keyword which has to be instance of the same class                
# THIS IS PERFECTLY LEGAL!!!
Test1.meth1 = Test1.meth2
Test1().meth1() # Test1.meth2()

# invoking method as object attribute (which in fact it is!)
getattr(Test1(),'meth1')()
(Test1().meth1)() # as attribute also


