'''
Created on 14 mar 2014

@author: Dominik

Here we have function decorators

'''

#### SIMPLE DECORATOR #########################
def decoratorFunc1(func):
    def inner(intNum):
        return func(intNum) + 1
    return inner

# HOW IT WORKS BASICALLY:
# 1) myDecorated1 is changed like: myDecorated1 = decoratorFunc1(myDecorated1)
# 2) decoratorFunc1() gets function as parameter, so that you can invoke it inside decorator
# 3) decoratorFunc1() defines inner() function that is returned, and inner() replaces myDecorated1()

@decoratorFunc1
def myDecorated1(someInt):
    return someInt*2

print "With decorator: ", myDecorated1(2); # prints 5 because it evaluates to myDecorated1(2)+1

#### USEFUL DECORATOR WITH VAR ARGS 
# This logger will log arguments of every function that is decorated by it
def logger(func):
    def inner(*args, **kwargs):
        print "Arguments of the function", func, " were: %s, %s" % (args, kwargs)
        # here we pass args list as var-args to func, and typed-args as typed args
        return func(*args, **kwargs)
    return inner

@logger
def testArgs(arg1, arg2, arg3):
    return arg1+arg2+arg3

print testArgs(5,6,7)
