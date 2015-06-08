## Python doesn't have abstract keyword, but you can write your own in following way:

def abstract():
    import inspect
    caller = inspect.getouterframes(inspect.currentframe())[1][3]
    raise NotImplementedError(caller + ' must be implemented in subclass')

class MyAbstractClass:
    def method1(self): abstract()

class MyClass(MyAbstractClass): 
    pass

class MyClassOK(MyAbstractClass): 
    def method1(self):
        print "MyClassOK.method1()"

# MyClass().method1() # NotImplementedError: method1 must be implemented in subclass
MyClassOK().method1() # MyClassOK.method1()