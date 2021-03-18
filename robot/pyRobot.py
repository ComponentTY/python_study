import requests
import json
from wxpy import *

robot = Bot()
my_friend = robot.friends().search('不谙世事的姑娘')[0]


def talk_robot(info='你好'):
    apiurl = 'http://10.192.26.23:80/robot'
    data = {
        'message': info
    }
    res = requests.post(apiurl, json=data).text
    retry = res
    return retry


@robot.register(my_friend)
def reply_myfriends(msg):
    message = msg.text
    replys = talk_robot(info=message)
    msg.reply(replys)


robot.start()
embed()
