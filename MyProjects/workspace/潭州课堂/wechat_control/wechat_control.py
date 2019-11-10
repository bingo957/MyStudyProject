#!/usr/bin/python3
# @Time      : 2019/7/14 14:07
# @Author    : 老杨
# @FileName  : wechat_control.py
# @Software  : PyCharm
# 全局作用域
# 局部作用域
import itchat
import os
import cv2
from PIL import ImageGrab
import Control


# 截屏的方法
def screen(fileName='screen.png'):
    im = ImageGrab.grab()
    im.save(fileName)
    itchat.send_image(fileName, 'filehelper')

# 打开电脑的软件


# 关机操作
def cmd(text='shutdown /s /t 0'):
    # 立即关机
    os.system(text)


# 拍照操作
def photo(fileName='laoyang.jpg'):
    # 调用电脑的第一个摄像头
    cap = cv2.VideoCapture(0)
    # 读取摄像头的资源
    # 第一个返回值表示是否成功读取到摄像头
    # True False
    # 第二个返回值 读取到的资源
    ret, img = cap.read()
    # 判断是否成功读取
    if ret:
        # 将读取到的资源生成一张照片
        cv2.imwrite(fileName, img)
        # 将照片发送给文档助手
        itchat.send_image(fileName, 'filehelper')
    else:
        itchat.send('读取摄像头失败', 'filehelper')
    # 释放摄像头
    cap.release()


def exe(text):
    ctrl = Control.Order()
    ctrl.run(text)


# 尽量避免全局变量，尽量采用函数传参的形式
# 1.代码可读性不高
# 2浪费空间
def control(text):
    # 控制电脑
    if text == '关机':
        cmd()
    if text == '拍照':
        photo()
    if text == '截屏':
        screen()
    else:
        exe(text)


# # 全局变量
# flag = False
"""
作用域分为全局和局部
函数体内的为局部，只能在本函数体内使用
全体的可以在任意位置使用
简单的举例：你自己的房间电脑只能你使用，而放在客厅的电脑，谁都可以使用
声明就是给你一把钥匙，允许你去更改它

函数体内获取函数体外的变量的方式：作为参数传递和全局作用域
尽量避免全局变量来传递
容易引起混乱，出错，也不利于代码的可读性
函数不可能总处于被动用的状态，而全局变量就需要占用空间，浪费空间
"""
# # 尽量避免全局变量，尽量采用函数传参的形式
# # 1.代码可读性不高
# # 2浪费空间
# def control(text):
#     # 声明全局变量，可以改写的目标
#     global flag
#     if text=='on':
#         flag = True
#     if text == 'off':
#         flag = False
#     if flag:
#         # 控制电脑
#         if text=='关机':
#             cmd()
#         if text == '拍照':
#             photo()
#         else:
#             # 提高程序的健壮性
#             # 避免程序中断
#             try:
#                 cmd(text)
#             except:
#                 itchat.send('您的指令有误','filehelper')
#     else:
#         itchat.send('您需要先发送 on 打开操控','filehelper')

# 消息注册机制
@itchat.msg_register(['Text'])
def message(msg):
    print(msg)
    # 提取出消息内容
    data = msg['Text'].strip()
    FromUserName = msg['FromUserName']
    # 提取出消息是发给谁的
    ToUserName = msg['ToUserName']
    # 提升用户体验
    # 当自己给自己发送了一条消息，就让文件助手自动跳出来
    if FromUserName == ToUserName:
        # 微信发送消息
        itchat.send('您现在可以操控了', 'filehelper')
    if ToUserName == 'filehelper':
        # 控制电脑
        # 提高代码的可读性，方便阅读
        # 方便调用
        control(data)
    print(data)


# 定义一个主函数
def main():
    # 占位符
    # 业务主逻辑
    # 登录微信  热加载 避免重复扫码
    # 会生成一份itchat.pkl的文件，用来保存登录信息
    itchat.auto_login(hotReload=True)
    # 让微信运行起来
    itchat.run()
# # 作为程序主入口
# 方便代码调试
# # __name__是我们python的一个内建变量


if __name__ == '__main__':
    # 证明是在当前脚本下运行
    main()
# print(__name__)
# 业务的主线
