'''
Created on 14 mar 2014

@author: Dominik

IMPORTANT!!!
List works like arrays in JavaScript, you can manipulate them, iterate over them,
sort them etc..

'''

class Lists(object):
    '''
    classdocs
    '''


    def __init__(self, params=None):
        '''
        Constructor
        '''
        
    def listVSTuple(self):
        print "------- listVSTuple() -------"
        # main difference is that list is changeable
        simpleTup = (1,2,3,4,5)
        simpleList = [1,2,3,4,5]
        # access is the same
        print simpleTup[1], " vs ", simpleList[1] # 2  vs  2
        print simpleTup[:3], " vs ", simpleList[:3] # (1, 2, 3)  vs  [1, 2, 3]
        # modifications are available for list
        ###  INSERT ELEMENTS
        simpleList.insert(1, 22)
        print simpleList # [1, 22, 2, 3, 4, 5]
        ###  INSERT OTHER LISTS
        simpleList.extend([11,12,13]) # extends list by another list
        print simpleList # [1, 22, 2, 3, 4, 5, 11, 12, 13]
        ### SORTING
        simpleList.sort();
        print simpleList # [1, 2, 3, 4, 5, 11, 12, 13, 22]
        ### COUNTING ELEMENTS
        simpleList.append(11) # here we append 11 to the end of list
        print simpleList.count(11) # 2
        ### GETTING LIST SIZE
        print "List has: ", len(simpleList), " elements"
        
    def fillingList(self):
        print "------- fillingList() -------"
        ##### this will pass "i" to list 5 times
        list1 = [i for i in range(5)] 
        print list1 # [0, 1, 2, 3, 4]
        ###### this will pass each element of list1 to list2 multiplied by 2
        list2 = [i*2 for i in list1]
        print list2 # [0, 2, 4, 6, 8]
        ##### more complex example
        # this will pass only even numbers to list3, odd will be converted to None
        list3 = [ list1[i] if list1[i]%2==0 else None for i in list1 ]
        print list3 # [0, None, 2, None, 4]
        ##### using defined function to fill the list
        def myFunc(i):
            if i==0: return None
            else: return i*10
        list4 = [myFunc(i) for i in list1]
        print list4 # [None, 10, 20, 30, 40]
    
    '''
        IMPORTANT!!
        This works EXACTLY THE SAME FOR TUPLES
    '''
    def slicingList(self):
        print "------- slicingList() -------"
        testS = ["one", "two", 3, 4, "5-five", "6-six"]
        print testS
        print "elements 1-2:\t\t\t", testS[1:3] # last is exlusive
        print "-3 element (off end):\t\t", testS[-3]
        print "last 3 elements:\t\t", testS[-3::]
        print "from 0 to -3:\t\t\t", testS[:-3]
        print "step iteration, every step +2: ", testS[::2]
        print "reversed :\t\t", testS[::-1]
        print "reversed, -4 to end:\t\t", testS[4::-1]
        print "reversed, -4 to +2 reversed:\t\t", testS[4:2:-1]
        
    def removingCertainElements(self):
        print "------- removingCertainElements() -------"
        a = [-1, 1, 66.25, 333, 333, 1234.5]
        del a[2:4] # del elements indexed: 2,3
        print a # [-1, 1, 333, 1234.5]
        
        
obj = Lists()
obj.listVSTuple()
obj.fillingList()
obj.slicingList()
obj.removingCertainElements()