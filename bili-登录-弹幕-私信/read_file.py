import os
import json

def read_dm(av):
    av = str(av)
    if os.path.isfile(os.getcwd()+'/av'+av+'_dm.txt'):
        with open('av'+av+'_dm.txt', 'r') as f: 
            file_list = json.loads(f.read())
        return file_list
    else:
        return []

def read_cookic():
    if os.path.isfile(os.getcwd()+'/cookic.txt'):
        with open('cookic.txt', 'r') as f:
            t = f.read()
        return t
    else:
        print('你应该设置 cookic \n 创建 cookic.txt 文件，并将你的 cookic 写入其中')
        exit()



def read_content():
    if os.path.isfile(os.getcwd()+'/content.txt'):
        with open('content.txt', 'r') as f: 
            file_list = f.readlines()
            # print(file_list,len(file_list))
        return file_list
    else:
        return ['']
