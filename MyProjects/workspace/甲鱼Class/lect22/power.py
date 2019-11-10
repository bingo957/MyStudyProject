"""
计算x的y次幂
"""


def power(x, y):
    if y == 1:
        return x
    else:
        return power(x, y - 1) * x


print(power(2, 10))
