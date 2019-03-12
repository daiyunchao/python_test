# -*- coding: utf-8 -*-
# 目标: 实现微信发消息功能
from wxpy import *
bot = Bot(console_qr=2,cache_path="botoo.pkl")

# 给"文件传输助手"发消息
my_friend = bot.file_helper.send('hello world')

# @bot.register()
# def print_others(msg):
#     print(msg)

# embed()
# 打印好友列表
# print bot.friends()

# 给指定好友发消息
# my_friend= bot.friends().search('lp')[0]
# my_friend.send('Hello WeChat!')
# my_friend.send_image('./wallhaven_images/2_wallhaven_01.jpg')

