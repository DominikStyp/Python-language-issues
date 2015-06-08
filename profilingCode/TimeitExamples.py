'''
Created on 17 mar 2014

@author: Dominik
'''

class TimeitExamples(object):
    '''
    classdocs
    '''


    def __init__(self, params=None):
        '''
        Constructor
        '''
    
    ''' WARNING! Indentations are important in setup string '''
    def ex1(self):
        import timeit
        setup = """
global A,B
A = 1
B = 2

def foo(num1, num2):
    pass

def mainprog():
    global A,B
    for i in range(20):
        # do something to A and B
        foo(A, B)
"""
        t = timeit.Timer(stmt="mainprog()", setup=setup)
        print(t.timeit(10000))
        
    def ex2(self):
        def f(x):
            return x * x
        import timeit
        print timeit.repeat("for x in range(100): lambda x: x*10","",
                  number=100000) 
        
        
        
        
obj = TimeitExamples()
obj.ex1()
obj.ex2()