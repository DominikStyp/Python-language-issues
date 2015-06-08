'''
Created on 18 mar 2014

@author: Dominik

REMEMBER:
If class defines methods __get__, __set__, __delete__ it's called descriptor
If an object defines both __get__ and __set__, it is considered a data descriptor
Descriptors that only define __get__ are called non-data descriptors
'''

class DescriptorDefinition(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
    def __get__(self, obj, typeV=None):
        pass
    
    def __set__(self, obj, value):
        pass
    
    def __delete__(self, obj):
        pass
