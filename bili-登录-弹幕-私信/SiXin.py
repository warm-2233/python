import os
import re
import time
import json
import random
import requests as req

import login
import read_file


# https://api.vc.bilibili.com/web_im/v1/web_im/send_msg
def csrf():
    k = read_file.read_cookic()
    cs = re.findall(r'bili_jct=(.*?);',k)[0]
    return cs

def send(uid, receiver_id, con):
    data = {
        'msg[sender_uid]': uid,
        'msg[receiver_id]': receiver_id,
        'msg[receiver_type]': '1',
        'msg[msg_type]': '1',
        'msg[msg_status]': '0',
        'msg[content]': '{"content":"'+con+'"}',
        'msg[timestamp]': int(time.time()),
        'build': '0',
        'mobi_app': 'web',
        'csrf_token': csrf(),
        }
    # print(data)
    url = 'https://api.vc.bilibili.com/web_im/v1/web_im/send_msg'
    res = req.post(url, headers=login.headers,data=data)
    if json.loads(res.text).get('code') == 0:
        print('发送成功',receiver_id)

        

def send_for(new_dm_list,uid, t=2):
    print('--')
    new_dms = new_dm_list[:]
    dm_list = read_file.read_dm(new_dms[0]['aid'])
    for dm in new_dm_list:  # 排除已有的弹幕
        if dm in dm_list:
            new_dms.pop(new_dms.index(dm))
    
    for i in new_dms:
        # 你应该在这里修改私信内容，想用 content.txt 中的内容你就不要把 {random_content()} 删除
        con = f'''
您好：{i['uname']} ，
您在 av{i['aid']} 视频 ，
于 {time_ymd(i['ctime'])} 时间，
发送弹幕： {i['msg']} 。
感谢您对我的支持。
-----------------------------------
我想对你说：
{random_content()}
'''
        # con = '以上为程序自动发送，请不要在意，谢谢，打扰您了！！'
        send(uid, i['mid'],con)
        time.sleep(t)
        
    print("over")
    write_dm_file(new_dm_list,new_dm_list[0]['aid'])
    
def time_ymd(t):
    # 获得当前时间时间戳
    now = int(t)
    #转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
    timeArray = time.localtime(now)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    # print(otherStyleTime)
    return otherStyleTime


def write_dm_file(b, av):
    with open('av'+str(av)+'_dm.txt','w') as f:
        f.write(json.dumps(b))

def random_content():
    con = read_file.read_content()
    return random.choice(con)
    

if __name__ =='__main__':
    pass
    
