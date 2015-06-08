'''
Created on 21 mar 2014

@author: Dominik
'''

# http://docs.python.org/2/library/itertools.html

import itertools as _i

class Itertools(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        #import sys
        #print(sys.version)
        
        
    # prints permutations of elements set
    def permutations(self):
        print "------ permutations() ------"
        nums = [0,1,2]
        # [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]
        print list(_i.permutations(nums))
    
    # prints x-sized combinations of elements set, no repeated elements
    def combinations(self):
        print "------ combinations() ------"
        nums = [0,1,2]
        # [(0, 1), (0, 2), (1, 2)]
        print list(_i.combinations(nums,2))
    
    # prints x-sized combinations of elements set, with repeated elements    
    def combinationsWithReplacement(self):
        print "------ combinationsWithReplacement() ------"
        nums = [0,1,2]
        # [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]
        print list(_i.combinations_with_replacement(nums,2))
    
    # filters elements which return False by lambda expression 
    def iffilter(self):
        print "------ iffilter() ------"
        # [1, 3, 5, 7, 9]
        print list(_i.ifilter(lambda x: x%2, range(10)))
        
    # works like nested for loops
    def product(self):
        # this is the same as nested loops over the sets:
        # ((x,y) for x in A 
        #            for y in B)
        for x,y in _i.product('ABC', 'xy'):
            # Ax  Ay Bx By Cx Cy            
            print x,y
            
    # makes INIFIT generator, if you won't break the loop,
    # it will iterate endlessly, producing: A B C D A B C D A B.....
    def cycle(self):
        # gen1 = _i.cycle('ABCD')
        gen1 = _i.cycle('ABCD')
        for x in range(0,10): # here we have only 10 passes of generator
            print gen1.next()
      
    # repeating one object mutliple times      
    def repeat(self):
        # AAAAAAAAAA
        for x in _i.repeat("A",10):
            print x
        
    ### GROUP BY doesn't work like SQL's
    ### but it can group elements like in following examples
    
    def groupby(self):
        # [['A', 'A', 'A', 'A'], ['B', 'B', 'B'], ['C', 'C'], ['D']]
        print [list(g) for k, g in _i.groupby('AAAABBBCCD')]   
        # ['A', 'B', 'C', 'D'] 
        print [k for k, g in _i.groupby('AAAABBBCCD')]
        
        
    def groupby1(self):
        things = [("animal", "bear"), 
                  ("animal", "duck"), 
                  ("plant", "cactus"), 
                  ("vehicle", "speed boat"), 
                  ("vehicle", "school bus")]
        '''
        A bear is a animal.
        A duck is a animal.
         
        A cactus is a plant.
         
        A speed boat is a vehicle.
        A school bus is a vehicle.
        '''
        for key, group in _i.groupby(things, lambda x: x[0]):
            print " ----- group ", key, " -------"
            for thing in group:
                print "A %s is a %s." % (thing[1], key)
                
    def groupby2(self):
        list1 = range(12)
        # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        print list1
        '''
            0 [0, 1, 2, 3, 4]
            1 [5, 6, 7, 8, 9]
            2 [10, 11]
        '''
        for key, igroup in _i.groupby(list1, lambda x: x // 5):
            print key, list(igroup)
        
            

    
    
obj = Itertools()
#obj.permutations()
#obj.iffilter()
#obj.combinations()
#obj.combinationsWithReplacement()
#obj.cycle()
#obj.groupby()
#obj.groupby2()
obj.product()
#obj.repeat()