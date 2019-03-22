from dealMsg import handelReply


def nowOnFriends():
    returnMsg = "当前发送自动脚本好友：\n"
    for line in handelReply.userNameArr:
        returnMsg = returnMsg + line + '\n'
    return returnMsg


def status(friend, group):
    returnMsg = f"私聊脚本状态：{friend}\n群聊脚本状态：{group}\n"
    returnMsg = returnMsg + nowOnFriends()
    return returnMsg
