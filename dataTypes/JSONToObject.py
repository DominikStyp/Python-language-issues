'''
Created on 19 mar 2014

@author: Dominik
'''

  
class JSONToObject(object):
    def __init__(self, d):
        for a, b in d.iteritems():
            if isinstance(b, (list, tuple)):
                setattr(self, a, [JSONToObject(x) if isinstance(x, dict) else x for x in b])
            else:
                setattr(self, a, JSONToObject(b) if isinstance(b, dict) else b)
    ## @Dominik: added iteritems allowing to iterate over dictionary 
    ## added because of code fragment: "JSONToObject(x) if isinstance(x, dict)"
    ## which returns JSONToObject instance instead of dict, so it can't be iterated in loop like regular dictionary
    ## x-key, y-value
    def iteritems(self):
        for x,y in self.__dict__.iteritems():
            yield (x,y)
    ## to eliminate need of using .iteritems() in every loop, I've implemented iterable here:
    def __iter__(self):
        return self.iteritems()
    
### example 1
d = {'a': 1, 'b': {'c': 2}, 'd': ["hi", {'foo': "bar"}]}
print "-------- example 1 -----------"
obj = JSONToObject(d)
print obj.a
print obj.d
print obj.d[1].foo

### example 2 ... more life-example
user = {"id":33, "name": "Ann", "hobbyList": ["swimming", "jogging", ["guitar","piano"] ], "languages": {"en": "perfect", "fr": "weak"} }
userObj =  JSONToObject(user)
print userObj.id
print userObj.hobbyList[0]
print userObj.hobbyList[2][0]

# using method JSONToObject.__iter__()
for n,v in userObj.languages:
    print "language: ", n, " level: ", v
    
# following example without using __iter__, but has to get access to __dict__.iteritems()     
# for n,v in userObj.languages.__dict__.iteritems():
#     print "language: ", n, " level: ", v
