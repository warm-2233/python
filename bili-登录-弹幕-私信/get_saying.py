import os
import json
import requests as req



def get_sa():
    url = 'https://api.shino.cc/hitokoto/?encode=json'
    h ={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    res = req.get(url,headers=h)
    return json.loads(res.content).get('hitokoto')


# print(get_sa())
'''
while 1:
    with open('content.txt','a') as f:
        a = get_sa()
        print(a)
        f.write(a+'\n')

'''