#coding:utf-8
'''
- 接入钉钉API接口，将错误的信息发送到相关负责人
'''
import json
import requests
import pymongo
import datetime
from datetime import isoformat

#connect influxDB 
conn = pymongo.MongoClient('mongodb://127.0.0.1:20000/')
db = conn.countly

#时间重组
now = datetime.datetime.now()
start = now.strftime('%Y-%m-%d %H:%M:%S')
date = now.strftime('%Y%m%d')
date1 = now.strftime('%Y')
date2 = now.strftime('%m')
date3 = now.strftime('%d')

date4 = datetime.datetime(int(date1),int(date2),int(date3))

#MongoDB查询
xstzaz = db.app_crashes599d1f85a0277904826181de.find({"cd":{"$gte":date4}}).count()
xstzios = db.app_crashes59ba3ca968a52f14b1e83023.find({"cd":{"$gte":date4}}).count() #统计时间大于等于当前之间的值

def send_msg():
    url = "https://oapi.dingtalk.com/robot/send?\
           access_token=f69d6e0aa163266f83e3ff7c59ed9803a872b0bf8518bbf90f64fda5a54f0a1a" #钉钉机器人Api接口
    header = {
                "Content-Type": "application/json",
                "charset": "utf-8"
             }
    
    if xstzaz or xstzios:
        data = {
                "msgtype": "markdown",
                "markdown": {
                             "title":"[每日崩溃简报]",
                             "text":
                                 "### 每日app崩溃简报(%s):\n\t"%(start,) +
                                 "1.鑫圣投资android %s次崩溃; \n\t"%(xstzaz,) +
                                 "2.鑫圣投资IOS %s 次， \n\n"%(xstzios,) +
                                 "> ![screenshot](http://www.linuxprobe.com/wp-content/uploads/2016/10/nodejs.png))\n"  +
                                 "> 请及时登录平台解决! \n" +
                                 "###### [崩溃报告](https://apm.magiccompass.cn:65480/)\n" +
                                 "> 本简报由机器人自动发布！"
                             },
                "at": { 
                        "atMobiles":[
                                    "18629502415",
                                    ],
                        "isAtAll": False 
                       }
                }
        sendData = json.dumps(data)
        R = requests.post(url, data=sendData, headers=header)
        
        print(R.text)
    else:
        print("No data Post!")
        exit(0)


if __name__ == "__main__":
    send_msg()