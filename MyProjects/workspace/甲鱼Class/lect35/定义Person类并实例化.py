"""
属性：姓名(默认姓名为“小甲鱼”)
方法：打印姓名
提示：方法中对属性的引用形式需加上sef,如 self name
"""


class Person:
    name = ''

    def print_name(self):
        print(self.name)
