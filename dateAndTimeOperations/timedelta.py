'''
Created on 27 mar 2014

@author: Dominik
'''
import unittest
from datetime import timedelta, datetime

# A timedelta object represents a duration, the difference between two dates or times

class Test(unittest.TestCase):


    def testEx1(self):
        print "------ testEx1() ------"
        print "min: ", timedelta.min
        print "max: ", timedelta.max
        print "no params: ", timedelta()
        print "-10 min " , timedelta(minutes = -10)
        print "year: ", timedelta(days=365)
        print "another year:",timedelta(weeks=40, days=84, hours=23, minutes=50, seconds=600)
        
    def testMathOperationsOnTimedelta(self):
        print "------ testMathOperationsOnTimedelta() -----"
        print timedelta(days=5) * 2 # 10 days, 0:00:00
        print timedelta(days=5) + timedelta(weeks=3) + timedelta(seconds=10)# 26 days, 0:00:10
        # The floor is computed and the remainder (if any) is thrown away
        print timedelta(seconds=32)//3 # 0:00:10.666666
        print abs(timedelta(seconds=-30)) # 0:00:30
        
        
    def testDatesDifference(self):
        print "------ testDatesDifference() ------"
        #### shifting date 
        date1 = datetime.now()
        date2 = date1 - timedelta(days=5)
        print date1, " - 5 days = ", date2


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testEx1']
    unittest.main()