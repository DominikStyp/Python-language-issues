'''
Created on 26 mar 2014

@author: Dominik

This file contains examples and tips for using console

######## IMPORTING AND USING MODULES AND CLASSES FROM CONSOLE #########

# Main tip is to watch out of what you're importing
# If you import module but without class you will be confused 
# experiencing: TypeError: 'module' object is not callable for python object

# following example is WRONG, because you're importing module but not class inside of it
>>> from flowControl import TernaryOperator
http://domain.pl/script.php?param2=33&param1=22
>>> obj = TernaryOperator()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
TypeError: 'module' object is not callable

# following example is CORRECT, importing class from module of the same name as class
>>> from flowControl.TernaryOperator import TernaryOperator    
>>> obj = TernaryOperator()
>>> obj.ex2()
Dictionary x:  is empty 


############ LOOP EXAMPLES #########
# Remember to use indentations (tabs in console)
>>> for x in range(1,10):
...     op=urllib.urlopen(link)
...     op.close()


# Print lines into file (remember that int must be converted into string before concatenation)
>>> f=open("c:/python_test.txt","w")
>>> for i in range(1,90):
...     f.write(str(i)+")\n")
...
>>> f.close()




'''
