"""
属性：长和宽
方法：设置长和宽-> setRect(self)，获得长和宽-> detEct(sel)，获得面积-> getArea(self
提示：方法中对属性的引用形式需加上sef,如 self width
"""


class Rectangle:
    length = 5
    width = 4

    def set_rect(self):
        print('请输入长方形的长和宽...')
        self.length = float(input('长：'))
        self.width = float(input('宽：'))

    def det_ect(self):
        print('这个长方形的长是：%.2f,宽是：%.2f。' % (self.length, self.width))

    def get_area(self):
        return self.length * self.width
