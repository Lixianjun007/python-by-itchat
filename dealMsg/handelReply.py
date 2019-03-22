from typing import List

from pip._vendor.distlib.compat import raw_input

userNameArr = []


class handelReply:

    # 文件助手
    def filehelper(self, msg="私聊开启", status=0):
        return {
            '私聊开启': 1,
            '私聊关闭': 2,
            '私聊全部开启': 3,
            '群聊开启': 1,
            '群聊关闭': 2,
            '群聊全部开启': 3,
        }.get(msg, status)

    def readList(self):
        global userNameArr
        userNameArrTmp: List[str] = []
        for line in open("config/username.txt", 'r', encoding='UTF-8'):
            userNameArrTmp.append(line)
        userNameArr = userNameArrTmp
        print(userNameArr)

    # 添加
    def addFiends(self, msg):
        global userNameArr
        name = msg.replace('添加', '')
        userNameArr.append(name)
        f = open("config/username.txt", 'a', encoding='UTF-8')
        # newline = raw_input(name)
        f.write(f"{name}\n")
        f.close()
        print(userNameArr)
        return

    # 删除
    def delFriends(self, msg):
        global userNameArr
        name = msg.replace('剔除', '')
        if name in userNameArr:
            local = userNameArr.index(name)
            if isinstance(local, int):
                userNameArr.pop(local)
                with open("config/username.txt", "r", encoding="utf-8") as f:
                    lines = f.readlines()
                # print(lines)
                with open("config/username.txt", "w", encoding="utf-8") as f_w:
                    for line in lines:
                        if f"{name}" in line:
                            continue
                        f_w.write(line)
        name = name + "\n"
        if name in userNameArr:
            local = userNameArr.index(name)
            if isinstance(local, int):
                userNameArr.pop(local)
                with open("config/username.txt", "r", encoding="utf-8") as f:
                    lines = f.readlines()
                # print(lines)
                with open("config/username.txt", "w", encoding="utf-8") as f_w:
                    for line in lines:
                        if f"{name}" in line:
                            continue
                        f_w.write(line)
        print(userNameArr)
        return


groupNameArr = [
    # 瑞安第三交通委
    '@@826cb0998054591bce69cb8a8f00f04c2b7366b950501e6f5ea730ab56255236',
    # 渣男大波浪渣女锡纸烫
    '@@47fc14ba9531b0e76cc52b3c58680d5092acc7cdd4554f5a9f2359f4dfba51f4',
    # 相亲相爱一家人
    '@@8a84d657f26ac04478d7af62c6ccd0f0b1e2a074d8a3ffb03563ba4889d7420e',
    # 东湾七匹狼
    '@@6521495ab8ccbce240b894242a362314466112dc98f8dc0dcdf9c9e774fd9c48',
    # 小神龙俱乐部
    '@@5f7b7e63780e35e47c40c05d34c4bdd634aff18a33b5905efecdeac0205cf48b',
]
