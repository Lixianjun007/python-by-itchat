from hashlib import new

import itchat
from dealMsg import dealMsg, handelReply, commonReturn

# 1:开启  2：关闭   3：最大权限
GLOBAL_FRIEND = 1
# 1:开启   2：关闭   3：最大权限
GLOBAL_GROUP = 1
GLOBAL_SELF = ''


# 用于接收来自朋友间的对话消息  #如果不用这个，朋友发的消息便不会自动回复
@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    global GLOBAL_FRIEND, GLOBAL_GROUP
    global GLOBAL_SELF
    if msg['ToUserName'] == 'filehelper':
        return returnFilter(msg)
    if GLOBAL_SELF != msg['FromUserName']:
        print(msg['User']['RemarkName'] + '--' + msg['Text'])
    else:
        print('自己--' + msg['Text'])
    # 为了过滤自己
    if msg['ToUserName'] == msg['FromUserName']:
        GLOBAL_SELF = msg['FromUserName']
    if (msg['ToUserName'] == msg['FromUserName']) | (msg['FromUserName'] == GLOBAL_SELF):
        return

    # debugStatus(GLOBAL_FRIEND, GLOBAL_GROUP)
    if GLOBAL_FRIEND == 1:
        # //msg['User']['RemarkName']
        if len(msg['User']) > 2:
            if (handelReply.userNameArr.count(msg['User']['RemarkName'])) | (
                    handelReply.userNameArr.count(msg['User']['RemarkName'] + '\n')):
                return dealMsg.get_response(msg['Text'])
    if GLOBAL_FRIEND == 3:
        return dealMsg.get_response(msg['Text'])
    return


# 文件助手处理
def returnFilter(msg):
    global GLOBAL_FRIEND, GLOBAL_GROUP
    returnMsg = ''
    # 设置变量
    if '私聊' in msg['Text']:
        GLOBAL_FRIEND = handelReply.handelReply().filehelper(msg['Text'], GLOBAL_FRIEND)
    if '群聊' in msg['Text']:
        GLOBAL_GROUP = handelReply.handelReply().filehelper(msg['Text'], GLOBAL_GROUP)
    if '添加' in msg['Text']:
        handelReply.handelReply().addFiends(msg['Text'])
        returnMsg = commonReturn.nowOnFriends()
    if '剔除' in msg['Text']:
        handelReply.handelReply().delFriends(msg['Text'])
        returnMsg = commonReturn.nowOnFriends()
    if '状态' == msg['Text']:
        returnMsg = commonReturn.status(GLOBAL_FRIEND, GLOBAL_GROUP)
    # debugStatus(GLOBAL_FRIEND, GLOBAL_GROUP)
    itchat.send(msg['Text'] + '成功！\n' + returnMsg, 'filehelper')
    return


@itchat.msg_register([itchat.content.TEXT], isGroupChat=True)
# 用于接收群里面的对话消息
def print_content(msg):
    print(msg['Text'])
    print(msg['User']['NickName'])
    if (msg['ToUserName'] == msg['FromUserName']) | (msg['FromUserName'] == GLOBAL_SELF):
        return
    global GLOBAL_GROUP
    # debugStatus(GLOBAL_FRIEND, GLOBAL_GROUP)
    if GLOBAL_GROUP == 1:
        # //群聊过滤
        if handelReply.userNameArr.count(msg['User']['NickName']):
            return dealMsg.get_response(msg['Text'])
    if GLOBAL_GROUP == 3:
        return dealMsg.get_response(msg['Text'])
    return


def debugStatus(friend, group):
    out = f"friend: {friend} ,  group: {group} \n"
    print(out)
    return
