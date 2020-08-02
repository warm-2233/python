
import time

import login
import SiXin as sx



def main(aid=None):
    mid = login.login() # 登录,返回up 主的 ID

    if not aid:
        aid = login.get_new_video(mid) # 获取最新视频，返回aid

        
    oid = login.get_oid(aid) # 获取视频 oid 通过 aid 来

    dm_list = login.get_dm_json(oid) # 获取视频的所有弹幕

    sx.send_for(dm_list, mid, 1)    # 私信发送, 1 是延迟发送1秒


if __name__ =="__main__":
    '''
    我认为 你只需要改 aid 即可
    只能使用自己的视频
    '''
    # main(710767291)
    while 1:
        main()
        time.sleep(120)

    
