### COMMAND TEMPLATE :
# >>> [command]
# [expected result]
### [expected result] is the output of command that test expects after invoke [command]

'''
Created on 19 mar 2014


>>> obj = Doctest1()
>>> obj.sumArgs(1,2,3)
6
>>> obj.sumArgs(1,-2,3)
1

'''
# first test is OK 
# second test:
# Failed example:
#    obj.sumArgs(1,-2,3)
# Expected:
#    1
# Got:
#    2


class Doctest1(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
    def sumArgs(self,*args):
        res = 0
        for x in args:
            res+=x
        return res


### very important is the following
if __name__ == "__main__":
    import doctest
    doctest.testmod()
        