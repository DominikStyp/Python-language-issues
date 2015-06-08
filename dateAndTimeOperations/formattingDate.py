'''
Created on 28 mar 2014

@author: Dominik
'''
import unittest
# WARNING! Module's name is exactly the same as class
from datetime import datetime


class Test(unittest.TestCase):


    def testFormatting(self):
        print "-------- testFormatting() --------"
        ### using string.format() where string is: "some string {:DATE_FORMAT}"
        print "Now is: {:%Y-%m-%d %H:%M:%S}".format(datetime.now())
        ### using strftime()
        print datetime.now().isoformat()
        # YYY-MM-DD HH:ii:ss in PHP
        print datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # month locale name, year without zero padded, 12-hour clock hour
        print datetime.now().strftime("%B, %y, %I")
        # decimal week num, PM/AM, time zone name (or empty), day of the year (zero padded)
        print datetime.now().strftime("%w, %p, %Z, %j")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testFormatting']
    unittest.main()