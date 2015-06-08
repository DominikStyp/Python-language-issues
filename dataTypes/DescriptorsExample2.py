'''
Created on 19 mar 2014

@author: Dominik
'''

class simpleDescriptor(object):
    
    data = {}
    default = None
    
    def __init__(self, default):
        self.default = default # setup default value for descriptor
    
    def __set__(self, instance, value):
        print "I'm setting value: ", value, " for instance: ", instance
        self.data[instance] = value
        
    def __get__(self, instance, owner):
        # dictionary's .get(key, defaultValue) method is used only to return self.default value, 
        # if there is no value at "instance" key
        print "I'm getting value from: ", instance, " owner: ", owner
        return self.data.get(instance, self.default)
        


class DescriptorsExample2(object):
    '''
    classdocs
    '''

    descVal = simpleDescriptor(0)
    otherVal = 1
    
    def __init__(self, param):
        '''
        Constructor
        '''
        self.descVal = param
        
    def test(self):
        return __dict__["descVal"]


obj1 = DescriptorsExample2(10)
obj2 = DescriptorsExample2(12)
print "obj1.descVal: ", obj1.descVal
print "obj2.descVal: ", obj2.descVal 
print "descVal: ", obj1.__dict__

        