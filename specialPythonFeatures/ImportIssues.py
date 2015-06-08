'''
Created on 17 mar 2014

@author: Dominik
'''

# you can also import all methods in one instruction
# using module level import wildcard
# Java-like import static
# BUT YOU SHOULD AVOID WILDCARD IMPORTS!!
from base64 import *

## REMEMEBER!!! There are also RELATIVE IMPORTS
## navigation works like in windows/unix paths
# import . package1 -> this imports subpackage package1 from the same directory as current file
# import .. package2 -> this imports package2 one level up from current file
# from ..package2 import myClass -> this imports class myClass from package2 one level up from current file
 
class ImportIssues(object):
    '''
    classdocs
    '''


    def __init__(self, params = None):
        '''
        Constructor
        '''
    
    def useModuleLevelImport(self):
        # from wildcard import
        print b64encode("hell yeah")
    
    def examples(self):
        from urllib import urlopen, urlretrieve
        myUrl = urlopen("http://onet.pl")
        for x in range(0,9): 
            print myUrl.readline()
        # alternative 1:
        #     import urllib.urlopen
        #     myUrl = urllib.urlopen("http://onet.pl")
        # alternative 2:
        #     from urllib import urlopen as o_
        #     myUrl = o_("http://onet.pl")
        #
        


obj = ImportIssues()
# obj.examples()
obj.useModuleLevelImport()