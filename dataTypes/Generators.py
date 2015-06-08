'''
Created on 21 mar 2014

@author: Dominik
'''

class Generators(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    '''
        1) Generator is basically object that is iterable
        2) yield keyword returns new loop position in it
        3) it can be iterable ONE TIME PER GENERATOR INSTANCE
        4) if you want to iterate over it again 
           you have to create new generator object
        
    '''
    def makeSquaresGenerator(self, rangeNum):
        for x in range(rangeNum):
            z = x**2
            yield z
            # this will be invoked after yield
            # but REMEMBER, following +=1 won't change returned value
            # because only yield statement can return value from loop
            # and any statement after yield won't affect returned value
            z += 1
            print "--right after yield z is ", z
        # following code will be invoked after generator object
        # has no items to iterate over
        # but you shouldn't add any code after yield,
        # because if generator loop is broken, print won't be invoked
        print "---code after generator loop---"

    def testGenerator(self):
        list1 = []
        for num in self.makeSquaresGenerator(5):
            list1.append(num)
        return list1
    
    # infinite iterator
    # cycle('ABCD') --> A B C D A B C D A B C D ...
    # implementation comes from: 
    # http://docs.python.org/2/library/itertools.html#itertools.cycle
    def cycle(self,iterable):  
        saved = []
        for element in iterable:
            yield element
            saved.append(element)
            # added to see that saved is only filled once
            print saved 
        while saved:
            # while saved variable is still set
            # elements are looped here over and over 
            for element in saved:
                yield element
    


obj = Generators()
print obj.testGenerator() # [0, 1, 4, 9, 16]
