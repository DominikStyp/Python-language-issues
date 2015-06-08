'''
Created on 14 mar 2014

@author: Dominik
'''

class FileOperations(object):
    '''
    classdocs
    '''
    
    filePath = ""
    fileWrapper = None
   
    def __init__(self, filePath):
        '''
        Constructor
        '''
        # r+ = read/write, r = only read, w = only write
        self.fileWrapper = open(filePath,"w+")
    
    # basic destructor, if object is destructed, fileWrapper is closed
    def __del__(self):
        self.fileWrapper.close()
        
    def fileExists(self,fPath):
        import os.path
        return os.path.isfile(fPath)
     
    def read(self):
        self.fileWrapper.seek(0)
        return self.fileWrapper.read()
            
    def write(self, strWrite):
        self.fileWrapper.seek(0)
        self.fileWrapper.write(strWrite)
        
    def close(self):
        self.fileWrapper.close()
    
    # safety read not using fileWrapper
    # with guarantees to close the file after instructions in with statement
    def _readUsingWith(self):
        strRead = ""
        with open(self.filePath) as f:
            strRead += f.read()
        return strRead
    # as above, write to file using with, which closes file after operation
    def _writeUsingWith(self,strWrite):
        with open(self.filePath) as f:
            f.write(strWrite)
    
    #### SERIALIZE OBJECT TO FILE ####################    
    def serialize(self,obj):
        import pickle
        self.fileWrapper.seek(0)
        pickle.dump(obj, self.fileWrapper)
    
    def unserialize(self):
        import pickle
        self.fileWrapper.seek(0)
        return pickle.load(self.fileWrapper)
    
    ##### JSON ENCODE/DECODE #########################
    def jsonToFile(self,jsonObj):
        import simplejson
        self.fileWrapper.seek(0)
        simplejson.dump(jsonObj, self.fileWrapper)
        
    def jsonFromFile(self):
        import simplejson
        self.fileWrapper.seek(0)
        return simplejson.load(self.fileWrapper)



#x = simplejson.loads(data)
    

class Foo(object):
    pass

#### examples ### 
## here we have example object that will be serialized by pickle module
testObj = Foo()
testObj.someVal = 1
testObj.tupleVal = (3,4,5,6)
testObj.listVal = [0,2,(1,2),3,4]

fileO = FileOperations('C:/pythonTestFile.txt')
##### SERIALIZE EXAMPLE ###################
## write object representation of the object to file
# fileO.serialize(testObj)
# read object from file
# testObj1 = fileO.unserialize()
# print "testObj1.tupleVal: ", testObj1.tupleVal 

##### JSON EXAMPLE #########################
testData = [ ['b','c'], {"dist":2}, (1,3,5) ]
fileO.jsonToFile(testData) # write JSON to file
testData1 = fileO.jsonFromFile() # read object from file
print "jsonFromFile: testData1[1].get('dist') ", testData1[1].get('dist')





