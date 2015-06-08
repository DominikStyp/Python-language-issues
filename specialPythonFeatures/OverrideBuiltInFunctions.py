

#### Following example overrides print function ##########
from __future__ import print_function
# This must be the first statement before other statements.
# You may only put a quoted or triple quoted string, 
# Python comments or blank lines before the __future__ line.

def print(*args, **kwargs):
    """My custom print() function."""
    # Adding new arguments to the print function signature 
    # is probably a bad idea.
    # Instead consider testing if custom argument keywords
    # are present in kwargs
    __builtins__.print('My overridden print() function!')
    return __builtins__.print(*args, **kwargs)


print ("lol", 1, 2, 3)