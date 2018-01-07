#coding:utf-8
'''
- 收集web端信息发送给钉钉
'''
import json
import requests
import datetime
from UseLibs import Timers,Logs

Logs.logger.debug("start program!")
now = datetime.datetime.now()
start = now.strftime('%Y-%m-%d %H:%M:%S')
date = now.strftime('%Y%m%d')
api_url = 'https://www.xsmcfx.com/'

#定时器设置,导入的是UseLibs下的Timers定时器
cron_time = 2
userlist = ["1773068***","1806691****"]

def check_url(url):
    client = requests.get(url)
    requests.adapters.DEFAULT_RETRIES = 5
    s = requests.session()
    s.keep_alive = False
    http_code = client.status_code
    http_time = client.elapsed.total_seconds()
    return http_code,http_time
    client.close()

requests.adapters.DEFAULT_RETRIES = 5
def send_msg():
    url = "https://oapi.dingtalk.com/robot/send?access_token=a91c216ece89737fab0dad1f8621e7cf1de09131cf38c960f26209e7cf624617"
    header = {
                "Content-Type": "application/json",
                "charset": "utf-8"
            }
    status,time  = check_url(api_url)
    if status != 200:
        data = {
                    "msgtype": "text",
                    "text":{
                            "content":"网站状态监测Robot(%s):\n网站访问或DNS存在异常！请及时排查！\n本简报由机器人自动发布！"%(start)
                            },
                    "at": {
                            "atMobiles": userlist,
                            "isAtAll": False
                            }
                }
        sendData = json.dumps(data)
        R = requests.post(url, data=sendData, headers=header)
        
    elif time > 1.0:
        print("延时过高超过1s!!")
    else:
        print("No data !")


if __name__ == "__main__":
    t = Timers.LoopTimer(cron_time,send_msg)
    t.start()