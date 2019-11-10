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
    def __init__(self):
        self.prompt = '未开始计时！'
        self.lasted = 0.0
        self.begin = 0
        self.end = 0
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

    # 开始计时
    def start(self):
        self.begin = self.defult_timer
        self.prompt = '请先调用stop()停止计时！'
        print('开始计时...')

    # 停止计时
    def stop(self):
        if not self.begin:
            print('请先调用start()开始计时！')
        else:
            self.end = self.defult_timer
            self._cal()
            print('计时结束!')

    # 内部方法计算时间
    def _cal(self):
        self.result = self.end - self.begin
        self.prompt = '总共运行了 %0.2f 秒' % self.result
        # 为下一轮计时初始化
        self.begin = 0
        self.end = 0

        # 用于启动计时器
        # def timing():
