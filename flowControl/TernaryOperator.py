'''
Created on 17 mar 2014

@author: Dominik
'''

class TernaryOperator(object):
    '''
    classdocs
    '''


    def __init__(self, params=None):
        '''
        Constructor
        '''
        
    def ex1(self):
        from urllib import urlencode
        str1 = "http://domain.pl/script.php"
        dict1 = {"param1": 22, "param2": 33}
        print str1+"?%s" % urlencode(dict1) if len(dict1)>0 else str1
        
    # very easy check if dictionary is empty or not
    def ex2(self):
        x = {}
        print "Dictionary x: ", x if x else "is empty "
        
        
        
obj = TernaryOperator()
obj.ex1()