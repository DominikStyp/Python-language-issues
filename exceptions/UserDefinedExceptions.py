'''
Created on 16 mar 2014

@author: Dominik
'''

class UserDefinedException(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
          '''
    def raiseUserDefinedException(self):
        try:
            raise UserInputError()
        except:
            print "UserInputError raised"
  
  
  
class Error(Exception):
    """Base class for exceptions in this module."""
    pass        
class UserInputError(Error):
    """Exception raised for errors in the input.
    
    Attributes:
        expr -- input expression in which the error occurred
        msg  -- explanation of the error
    """
    
    def __init__(self, expr, msg):
        self.expr = expr
        self.msg = msg


## examples
UserDefinedException().raiseUserDefinedException();