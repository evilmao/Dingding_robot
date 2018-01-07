#coding:utf-8
'''
- JIRA收集信息，通过钉钉机器人发送到指定的相关人
'''

import json
import requests
from ConfigData import Get_Jira
import datetime
from collections import __main__
now = datetime.datetime.now()
start = now.strftime('%Y-%m-%d %H:%M:%S')

def send_msg():
    url = "https://oapi.dingtalk.com/robot/send?access_token=10562c16dc602dc8225d5ffa5dd4c6a808f0d456e183d482763f5e2ed3137216"
    header = {
                "Content-Type": "application/json",
                "charset": "utf-8"
            }
    dtall = format(Get_Jira.get_issue())
    if dtall :

        data = {
                    "msgtype": "text",
                    #"title":"[每日逾期任务播报]",
                    "text":{ "content":"每日app逾期任务简报(%s):\n请及时处理相关问题!\n点击查看：http://jira.lan/issues/\n%s本简报由机器人自动发布！"%(start,dtall)},
                    "at": {
                            "atMobiles":Get_Jira.get_users(),
                            "isAtAll": False
                          }
                }
        sendData = json.dumps(data)
        R = requests.post(url,data=sendData,headers=header)

    else:
        print("No data Post!")
        exit(0)

if __name__ == "__main__":
    send_msg()        
send_msg()