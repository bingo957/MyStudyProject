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
import time


class MyDes:
    """
    记录指定变量的读取/修改操作，并将记录以及出发时间保存在 record.txt 中
    """
    def __init__(self, value, interval, name):
        self.val = value
        self.int = interval
        self.name = name
        self.filename = 'record.text'

    def __get__(self, instance, owner):
        with open(self.filename, 'a', encoding='UTF-8') as f:
            f.write('%s变量在北京时间%s被读取，%s=%s' % (self.name, time.ctime(), self.name, str(self.val)))
            return self.val

    def __set__(self, instance, value):
        with open(self.filename, 'a', encoding='UTF-8') as f:
            f.write('%s变量在北京时间%s被读取，%s=%s' % (self.name, time.ctime(), self.name, str(value)))
            self.val = value
