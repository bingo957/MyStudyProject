"""
该类代码适用于附在某个类中
"""


class C:
    count = 0

    def __init__(self):
        C.count += 1

    def __del__(self):
        C.count -= 1
