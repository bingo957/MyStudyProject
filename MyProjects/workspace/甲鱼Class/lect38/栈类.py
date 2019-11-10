"""
定义一个栈( Stack)类，用于模拟一种具有后进先出(uIFo)特性的数据结构。至少需要有以下方法：
isEmpty()  判断当前栈是否为空(返回True或 False)
push()     往栈的顶部压入一个数据项
pop()      从栈顶弹出一个数据项(并在栈中删除)
top()      显示当前栈顶的一个数据项
bottom()   显示当前栈底的一个数据项
"""


class Stack:
    def __init__(self, start=()):
        self.stack = []
        for i in start:
            self.push(i)
            # self.stack.append(i)

    def isEmpty(self):
        return not self.stack

    def push(self, obj):
        self.stack.append(obj)

    def pop(self):
        if not self.stack:
            print('警告！栈为空！')
        else:
            return self.stack.pop()

    def top(self):
        if not self.stack:
            print('警告！栈为空！')
        else:
            return self.stack[-1]

    def bottom(self):
        if not self.stack:
            print('警告！栈为空！')
        else:
            return self.stack[0]
