'''
Created on 14 mar 2014

@author: Dominik
'''

class ListOperationFunctions(object):
    '''
    classdocs
    '''
    def __init__(self, params):
        '''
        Constructor
        '''
        
    ''' Let's map array like array_map from PHP '''
    def mapExample(self):
        nums = [1,2,3,4] # define list
        # 1) define temporary lambda function that gets 1 param x and return x*2
        # 2) map lambda function over nums list and print result
        print " ----- mapExample() ----- " 
        print map(lambda x : x*2, nums)
        
    ''' zip function combines list into tuple pairs '''
    def zipExample(self):
        oddNums = [1,3,5]
        evenNums = [2,4,6]
        print " ----- zipExample() ----- "
        print zip(oddNums,evenNums) # [(1, 2), (3, 4), (5, 6)]
        
    ''' let's create factorial (PL=silnia) example using reduce
        reduce goes over all elements of the array 
        and combines results between each specialPythonFeatures
    '''    
    def reduceExample(self):
        nums = [1,2,3,4]
        print " ----- reduceExample(): factorial ----- "
        # it evaluates like: (((1*2)*3)*4)
        print reduce(lambda x,y : x*y, nums)
        
    def filterExample(self):
        nums = [1,2,3,4,5,6]
        print " ----- filterExample(): ----- "
        # filters odd numbers and leaves only even
        # if lambda function returns False element is removed from the list
        print filter(lambda x : True if x % 2 == 0 else False, nums) 

obj = ListOperationFunctions(0)
obj.mapExample();
obj.zipExample();
obj.reduceExample();
obj.filterExample();