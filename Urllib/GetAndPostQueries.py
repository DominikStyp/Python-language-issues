'''
Created on 16 mar 2014

@author: Dominik
'''



class GetAndPostQueries(object):
    '''
    classdocs
    '''

    url = ""
    def __init__(self, url):
        '''
        Constructor
        '''
        self.url = url
    
    # @param dictionary with get parameters
    def get(self,dict1):
        import urllib
        # this is ternary operator which works like:
        # @evaluate-and-return if @condicion else @evaluate-and-return
        urlStr = self.url+"?%s" % urllib.urlencode(dict1) if len(dict1)>0 else self.url
        #print urlStr
        f = urllib.urlopen(urlStr)
        return f.read()
    
    # @param dictionary with post parameters    
    def post(self, dict1):
        import urllib
        f = urllib.urlopen(self.url,dict1)
        return f.read()
    
    # example of using custom headers
    def getWithHeaders(self):
        import urllib2
        req = urllib2.Request('http://google.pl/')
        req.add_header('Referer', 'http://www.python.org/')
        r = urllib2.urlopen(req)
        return r.read()
        
obj = GetAndPostQueries("http://google.pl")
obj.get({"param1": 2, "param2": 3});
obj.post({"param1": 2, "param2": 3});
print obj.getWithHeaders()