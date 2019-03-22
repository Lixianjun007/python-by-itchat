# coding=utf-8
import threading
from time import sleep

import itchat

from dealMsg.handelReply import handelReply
from domain import sendMsg
from domain.GFWeather import gfweather


def run():
    gfweather().run()
    # gfweather()


if __name__ == '__main__':
    handelReply().readList()

    threading._start_new_thread(gfweather().run, ())
    threading._start_new_thread(itchat.run, ())
    sleep(2)
    msg = "操作指令：向文件传输助手发送\n1:私聊开启（白名单中的好友会收到自动回复脚本）\n2：私聊关闭（所有自动回复脚本关闭）\n3：私聊全部开启（全部好友都会收到自动回复脚本）\n4:群聊关闭（所有群聊关闭自动脚本）\n5：群聊全部开启（所有群聊开启自动回复脚本）\n6：添加{好友备注}（将好友添加至自动回复白名单）\n7：剔除{好友备注}（将好友移除白名单）\n8：状态（当前状态）"
    itchat.send_msg(msg, 'filehelper')
    while 1:
        itchat.configured_reply()
