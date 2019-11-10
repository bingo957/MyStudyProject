"""
递归十进制转二进制，采用取二取余的方法结果与调用bin一样返回字符串
"""


def dec2bin(num):
    result = ''
    if num:
        result = dec2bin(num // 2)
        return result + str(num % 2)
    else:
        return result


print(dec2bin(10))
