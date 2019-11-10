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
import time as t


class MyTimer:
    """
    此程序改进了计算时间的方式，不会出现负数，但默认一个月为31天。
    """
    def __init__(self):
        self.unit = ['年', '月', '日', '时', '分', '秒']
        self.borrow = [0, 12, 31, 24, 60, 60]
        self.prompt = '未开始计时！'
        self.lasted = []
        self.begin = 0
        self.end = 0

    def __str__(self):
        return self.prompt

    __repr__ = __str__

    def __add__(self, other):
        self.prompt = '总共运行了'
        self.result = []
        for index in range(6):
            self.result.append(self.lasted[index] + other.lasted[index])
            if self.result[index]:
                self.prompt += (str(self.result[index]) + self.unit[index])
        return self.prompt

    # def set_timer(self):

    # 开始计时
    def start(self):
        self.begin = t.localtime()
        self.prompt = '请先调用stop()停止计时！'
        print('开始计时...')

    # 停止计时
    def stop(self):
        if not self.begin:
            print('请先调用start()开始计时！')
        else:
            self.end = t.localtime()
            self._cal()
            print('计时结束!')

    # 内部方法计算时间
    def _cal(self):
        self.lasted = []
        self.prompt = "总共运行了："
        for index in range(5, -1, -1):
            temp = self.end[index] - self.begin[index]
            if temp < 0:
                self.end[index] += self.borrow[index]
                self.end[index - 1] -= 1
            self.lasted.insert(0, (self.end[index] - self.begin[index]))
        for index in range(6):
            if self.lasted[index]:
                self.prompt += (str(self.lasted[index]) + self.unit[index])
        # 为下一轮计时初始化
        self.begin = 0
        self.end = 0
