'''
Created on 22 mar 2014

@author: Dominik
'''
import unittest
import re

class Test(unittest.TestCase):


    # re.search() only searches for presence of pattern inside string
    # and doesn't match whole occurences of pattern
    def testSearch(self):
        print "------ testSearch() ------"
        # r'string' - means raw string
        # u'string' - means unicode string
        m = re.search(r'(?<=0b)\d+', "some bin nums 0b332 or 0b33")
        print "found bin numbers: ", m.group(0)
    
    # re.match() checks for a match only at the beginning of the string
    # REMEMBER!!! WHOLE STRING MUST MATCH PATTERN, NOT ONLY FRAGMENT
    def testMatch(self):
        print "------ testMatch() ------"
        m = re.match(r'.*(?<=0b)\d+.*', "some bin nums 0b332 or 0b33")
        if(m != None): print "I've found: ", m.group(0)
    
    def testMatchNamedGroups(self):
        print "------ testMatchNamedGroups() ------"
        m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds", re.MULTILINE)
        print "By group name: ", m.group('first_name'), m.group('last_name')
        print "All groups:", m.groups()
    
    # re.findall() finds all occurences of the pattern
    def testFindAll(self):
        print "------ testFindAll() ------"
        # remember: look behind/ahead doesn't capture parentheses
        m = re.findall(r'(?<=0b)\d+', "some bin nums 0b332 or 0b33")
        if(m != None): print m
        
    # re.finditer() allows to iterate over results as is instances of MatchObject
    def testFindIter(self):
        print "------ testFindIter() ------"
        # prints: 00-04: Mary  11-15: John
        # .start() gives INCLUSIVE start index
        # .end() gives EXCLUSIVE end index
        for matchObj in re.finditer(r"[A-Z]{1}\w+", "Mary knows John very well"):
            print '%02d-%02d: %s' % (matchObj.start(), matchObj.end(), matchObj.group(0))

    # splits string by regular expression            
    def testSplit(self):
        print "------ testFindIter() ------"
        print re.split('(\W+)', 'Words, words, words.')
            
    # re.sub() replaces every occurence of the pattern in string
    def testSub(self):
        print "------ testSub() ------"
        # we can define our own replace function
        self.mySum = 0
        def repl(matchObj):
            self.mySum += int(matchObj.group(0))
            return "'"+matchObj.group(0)+"'"
        result = re.sub(r"(\d+)", repl, "There are digits 1 and 22 or 33")
        print result, "Their sum is: ", self.mySum
        
    # if you pass re.DEBUG, you can easily see how regex is interpreted 
    def testDebugRegex(self):
        print "------ testDebugRegex() ------"
        re.match("[a-z]+", "this is ### some string", re.DEBUG)
        
        
    @staticmethod
    def displaymatch(match):
        if match is None:
            return None
        return '<Match: %r, groups=%r>' % (match.group(), match.groups())   
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main(verbosity=2)