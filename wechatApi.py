#-*- encoding:utf-8 -*-
'''
flask_wechat:使用flask微信API
'''
from flask_wechat import filters,WeChat

wechat = WeChat()

@wechat.account
def get_config(id):
    return dict(
        appid="appid",
        appsecrect="appsecret",
        token="token"
    ) if id == "demo" else dict()

@wechat.handler("demo",filters.event.subscribe)
def subscribe(message):
    return message.reply_text(u"感谢您的订阅！")

@wechat.handler("demo")
def all(message):
    return message.reply_text(u"测试阶段!")

@wechat.handler("demo",filters.message.startswith("hello"))
def hello(message):
    return message.reply_text(u"你好,世界!")