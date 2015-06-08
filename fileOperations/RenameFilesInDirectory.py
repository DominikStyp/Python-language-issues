'''
Created on 5 kwi 2015

@author: Dominik
'''


class MyClass(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def changeFileNames(self, dirPath, numberRegex):
        import re, os
        for dirr, dirs, filenames in os.walk(dirPath):
            for filename in filenames:
                
                old = os.path.join(dirr, filename)
                # "#14 blahBlah.txt" 
                new = os.path.join(dirr, re.sub(r'(.*?)' + numberRegex + '(.*?)', r'\2 \1\3', filename))
                print "Zamieniam " + old + " ====> " + new
                os.rename(old, new)

obj = MyClass()
# changes files like: "Skyrim blah blah Part 223.mp4" ===> "Part 223 Skyrim blah blah.mp4"
# (Part \d+) is the regex that will be prefix of the each file
obj.changeFileNames('H:/GRY-KOMPUTEROWE/Elder Scrolls V - Skyrim', '(Part \d+)')