'''
Created on 26 mar 2014

@author: Dominik
'''
# creating static variable is like creating function attribute
# and hasattr() checks whether attribute exists or not
def cnt():
        if not hasattr(cnt,"cntV"):
            cnt.cntV = 0
        cnt.cntV += 1
        return str(cnt.cntV)+")"