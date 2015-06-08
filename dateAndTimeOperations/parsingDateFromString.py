'''
Created on 28 mar 2014

@author: Dominik
'''
import unittest
from datetime import datetime


class Test(unittest.TestCase):


    def testParse(self):
        # parsing date according to format
        print datetime.strptime("2012-02-01 00:00:00", "%Y-%m-%d %H:%M:%S")
        print datetime.strptime('Wed, 27 Oct 1770 22:17:00', '%a, %d %b %Y %H:%M:%S')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()