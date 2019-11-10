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
"""
定义一个矩形类：
有默认两个属性 宽/高
当要修改的属性为 square 时，说明是个正方形，则 宽/高 均设为 value
"""


class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __setattr__(self, key, value):
        if key == 'square':
            self.width = value
            self.height = value
        else:
            # self.key = value 会陷入无限递归陷阱，可用以下两方法二选一
            super().__setattr__(key, value)  # 调用基类方法赋值
            self.__dict__[key] = value  # 用类的属性字典方法进行赋值
            # 当要定义属性 square 时，执行self.width = value；self.height = value操作，此时有会自动调用__setattr__，会转到else中去
            # 所以，不管是不是要修改 square ，这样都不会引起死循环

    def getArea(self):
        return self.width * self.height
