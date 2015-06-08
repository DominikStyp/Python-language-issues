'''
Created on 16 mar 2014

@author: Dominik
'''

class ExampleHandlers(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def division(self,dividend,divisor):
        print "----- division ----"
        try:
            return dividend/divisor
        except ZeroDivisionError:
            print "Whoops your divisor is 0. You cant divide by 0"
            return 0
        
    def openFileExample(self):
        import sys
        try:
            f = open('myfile.txt')
            s = f.readline()
            i = int(s.strip())
        # you can get exception information like this
        except IOError as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)
        except ValueError:
            print "Could not convert data to an integer."
        # you can catch every other exception that wasn't caught earlier
        except:
            print "Unexpected error:", sys.exc_info()[0]
            raise
        
    def mutlipleCatch(self):
        print "----- mutlipleCatch ----"
        try:
            return 1/0 
        except (RuntimeError, TypeError, NameError, ZeroDivisionError) as err:
            print "I've got message: {0}".format(err)
        
    def raisingExceptions(self, num):
        print "----- raisingExceptions ----"
        if num < 0:
            raise ValueError("You can't pass less than 0 value here")
        return num
    
    def catchOtherMethodException(self):
        print "----- catchOtherMethodException ----"
        try:
            self.raisingExceptions(-2)
        except ValueError as er:
            print "Value error occured: {0}".format(er)
        except:
            import sys
            print "Ooops error occured: {0}".format(sys.exc_info()[0])
        return True


## examples 
# print "Result is: ", ExampleHandlers().division(10, 0)
# ExampleHandlers().openFileExample()
ExampleHandlers().catchOtherMethodException()
ExampleHandlers().mutlipleCatch()


                    