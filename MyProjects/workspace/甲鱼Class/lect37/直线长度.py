"""
定义一个点( Point)类和直线(Line)类，使用 gehLen万法可以获得直线的长度
提示:
·设点A1Y1)、点B0X2Y2)，则两点构成的直线长度|AB|=根号(x1-x2)^2+(y1-y2)^2)
·Python中计算开根号可使用math模块中的sqrt函数直线需有两点构成，因此初始化时需有两个点( Point)对象作为参数
"""
import math


class Point:
    def __init__(self, p = (0,0)):
        self.x = p[0]
        self.y = p[1]


    def getx(self):
        return self.x


    def gety(self):
        return self.y


class Line:
    def __init__(self, p1, p2):
        self.point1 = Point(p1)
        self.point2 = Point(p2)
        self.x = self.point1.getx() - self.point2.getx()
        self.y = self.point1.gety() - self.point2.gety()
        self.len = math.sqrt(self.x * self.x + self.y * self.y)


    def get_len(self):
        return  self.len


line = Line((1, 1), (4, 5))
print(line.get_len())
