"""
1、可以传给函数多个字符串
2、字符类型包括英文字母、空格、数字、其它
"""
def count(*param):
    length = len(param)
    for i in range(length):
        letters = 0
        space = 0
        digit = 0
        others = 0
        for each in param[i]:
            if each.isalpha():
                letters += 1
            elif each.isdigit():
                digit += 1
            elif each == ' ':
                space += 1
            else:
                others += 1
        print('第 %d 个字符串共有：英文字符 %d 个，数字 %d 个，空格 %d 个，其他字符 %d 个。' % (i + 1, letters, digit, space, others))


count('I love Fishc.com', 'I love you,you love me')
