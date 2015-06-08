'''
Created on 8 lis 2014

@author: Dominik
'''
import json
import requests # musi byc zainstalowany przez python PIP np. w cmd wpisz "pip2.7 install requests"
for x in range(100,999):
    p = {'tel': str(x)+'222333'}
    u = 'http://video-stream.pl/s/php/formval1.php'
    requests.post(u,data=json.dumps(p))