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
    此程序对改进了时间计算，不会出现负数，并且每个月的天数也会自动改变。
    应用time模块中的, perf_counter():计时器的精准时间（系统的运行时间）
                     process_time():当前进程执行CPU的时间总和
    """
    def __init__(self, func, number=1000000):
        self.prompt = '未开始计时！'
        self.lasted = 0.0
        self.begin = 0
        self.end = 0
        self.func = func
        self.number = number
        self.defult_timer = t.perf_counter()

    def __str__(self):
        return self.prompt

    __repr__ = __str__

    def __add__(self, other):
        self.result = self.lasted + other.lasted
        self.prompt = '总共运行了 %0.2f 秒' % self.result
        return self.prompt

    def set_timer(self, timer):
        if timer == 'perf_counter':
            self.defult_timer = t.perf_counter()
        elif timer == 'perf_counter':
            self.defult_timer = t.process_time()
        else:
            print('输入错误，请输入 perf_counter 或 process_time')

    # 用于启动计时器
    def timing(self):
        self.begin = self.defult_timer
        for i in range(self.number):
            self.func()
        self.end = self.defult_timer
        self.lasted = self.end - self.begin
        self.prompt = '总共运行了 %0.2f 秒' % self.lasted

# 以下为测试程序，可利用上述类计算程序运行时间


"""
def test():
    text = 'I Love FishC.com!'
    char = '0'
    if char in text:
        pass
"""
# 调用命令


"""
t1 = MyTimer(test)
t1.timing()
ti
"""
