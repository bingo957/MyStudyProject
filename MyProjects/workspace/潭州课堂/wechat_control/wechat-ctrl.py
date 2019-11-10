#
#                 God Bless No Bugs!
#
#                       _ooOoo_
#                      o8888888o
#                      88" . "88
#                      (| -_- |)
#                      O\  =  /O
#                   ____/`---'\____
#                 .'  \\|     |//  `.
#                /  \\|||  :  |||//  \
#               /  _||||| -:- |||||-  \
#               |   | \\\  -  /// |   |
#               | \_|  ''\---/''  |   |
#               \  .-\__  `-`  ___/-. /
#             ___`. .'  /--.--\  `. . __
#          ."" '<  `.___\_<|>_/___.'  >'"".
#         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#         \  \ `-.   \_ __\ /__ _/   .-` /  /
#    ======`-.____`-.___\_____/___.-`____.-'======
#                       `=---='
#    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#
# coding: utf-8 #
#  author:李斌  #
import itchat
import os
import cv2
from PIL import ImageGrab
import Control


def shut_down():
    os.system('shutdown /s /t 0')


def photo():
    cap = cv2.VideoCapture(0)
    ret, img = cap.read()
    if ret:
        cv2.imwrite('photo.jpg', img)
        itchat.send_image('photo.jpg', 'filehelper')
    else:
        itchat.send('摄像头获取失败！', 'filehelper')
    cap.release()


def screen():
    scr = ImageGrab.grab()
    scr.save('screen.jpg')
    itchat.send_image('screen.jpg', 'filehelper')


def exe(text):
    ctrl = Control.Order()
    ctrl.run(text)


def control(text):
    if text == '关机':
        shut_down()
    if text == '拍照':
        photo()
    if text == '截屏':
        screen()
    else:
        exe(text)


@itchat.msg_register(['TEXT'])
def message(msg):
    data = msg['Text'].strip()
    FromUserName = msg['FromUserName']
    ToUserName = msg['ToUserName']
    if FromUserName == ToUserName:
        itchat.send('您现在可以发出指令了！', 'filehelper')
    if ToUserName == 'filehelper':
        control(data)


# 登陆/打开微信
def main():
    itchat.auto_login(hotReload=True)
    itchat.run()


if __name__ == '__main__':
    main()
