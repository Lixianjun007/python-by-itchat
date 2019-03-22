import requests


def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    # 改成你自己的图灵机器人的api，上图红框中的内容，不过用我的也无所谓，只是每天自动回复的消息条数有限
    data = {
        'key': 'a799964eb173413ab6698f2e37734c68',  # Tuling Key
        'info': msg,  # 这是我们发出去的消息
        'userid': 'wechat-robot',  # 这里你想改什么都可以
    }
    # 我们通过如下命令发送一个post请求
    r = requests.post(apiUrl, data=data).json()
    if r.get('text') == '亲爱的，当天请求次数已用完。':
        data = {
            'key': '15c73255f26e4f2cbf4f8bf0ba555953',  # Tuling Key
            'info': msg,  # 这是我们发出去的消息
            'userid': 'wechat-robot',  # 这里你想改什么都可以
        }
        # 我们通过如下命令发送一个post请求
        r = requests.post(apiUrl, data=data).json()
    msg = '李贤俊的助手：%s' % r.get('text')
    print(r.get('text'))
    return msg