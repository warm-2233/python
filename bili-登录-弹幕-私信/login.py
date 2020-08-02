import os
import re
import json
import requests as req

import read_file

cookie = read_file.read_cookic()
headers={}
headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
headers['cookie'] = cookie

def get_req(url):
    global headers
    res = req.get(url,headers=headers)
    return res
    

    

# https://api.bilibili.com/x/v1/dm/list.so?oid=2233        弹幕-XML

def login():
    url = "https://api.bilibili.com/x/web-interface/nav"
    res = get_req(url)
    txt = json.loads(res.text)
    # print(res.text)
    if txt.get('code') == 0:
        print('登录成功')
        return txt.get('data').get('mid')
    else:
        print('登录失败')
        return 0


def get_new_video(uid):
    url = f'https://api.bilibili.com/x/space/arc/search?mid={uid}&ps=30&tid=0&pn=1&keyword=&order=pubdate&jsonp=jsonp'
    res = get_req(url)
    txt = json.loads(res.text)['data']['list']['vlist'][0]
    new_vid = txt.get('aid')
    return new_vid


def get_oid(aid):
    url = f'https://member.bilibili.com/x/web/archive/parts?aid={aid}'
    res = get_req(url)
    txt = json.loads(res.text)['data']['part_list'][0]['cid']
    # print(txt)
    return txt
    


def get_dm_xml(oid):
    # oid = 196357179
    url = f'https://api.bilibili.com/x/v1/dm/list.so?oid={oid}'
    res = get_req(url)
    dm_list = re.findall(r'<d.+?>(.*?)<.d>', res.content.decode('utf-8'))
    # print(dm_list)
    return dm_list

def get_dm_json(oid):
    a =[]
    i = 1
    while True:
        url = f'https://api.bilibili.com/x/v2/dm/search?oid={oid}&type=1&keyword=&order=ctime&sort=desc&pn={i}&ps=50'
        res = get_req(url)
        txt = json.loads(res.text)
        if not txt.get('data').get('result'):
            return a
        # print(txt.get('data').get('result'))
        a.extend(txt.get('data').get('result'))
        i += 1


        

if __name__ == '__main__':
    pass
