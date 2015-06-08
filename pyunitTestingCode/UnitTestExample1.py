

''' 

To create unit test you have to do following:
New -> PyDev Module -> [give file name] -> Template -> Module: Unittest

If you want to see results of the tests, 
you have to run script with --verbosity=2 argument where 2 is level of verbosity 
    
--verbosity=number
Sets the verbosity level for the run

--jobs=number
The number of processes to be used to run the tests

--split_jobs=tests|module
if tests is passed (default), the tests will be split independently to each process
if module is passed, a given job will always receive all the tests from a module

An example of options that can be set in the preferences would be:

--verbosity=1 --jobs=2 --split_jobs=module
    
'''

def multiply(a, b):
    """
>>> multiply(4, 3)
12
>>> multiply('a', 3)
'aaa'
"""
    return a * b

import unittest

class TestUM(unittest.TestCase):
 
    # invoke before every method
    def setUp(self):
        print "\n---setUp---"
    # invoke after every test
    def tearDown(self):
        print "\n---tearDown---"
 
    def test_numbers_3_4(self):
        print "---multiplyTest---"
        self.assertEqual( multiply(3,4), 12)
 
    def test_strings_a_3(self):
        self.assertEqual( multiply('a',3), 'aaab')
 
if __name__ == '__main__':
    unittest.main(verbosity=3)