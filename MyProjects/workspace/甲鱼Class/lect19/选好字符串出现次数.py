"""
编写一个函数 findstr(),该函数统计一个长度为2的子宇符串在另一个宇符串中出现的次数。
例如：假定输入的宇符串为“ You cannot improve your past, but you can improve your future.
Once time is wasted, life is wasted.”，子宇符串为“im”，函数执行后打印“子宇母串在目标宇符串中共出现3次”。
"""


def findStr(desstr, substr):
    count = 0
    length = len(desstr)
    if substr not in desstr:
        print('在目标字符串中未找到子字符串！')
    else:
        for each in range(length - 1):
            if desstr[each] == substr[0]:
                if desstr[each + 1] == substr[1]:
                    count += 1
        print('在目标字符串中共有子字符串 “%s” %d 个' % (substr, count))


desStr = input('请输入目标字符串：')
subStr = input('请输入两位子字符串;')
findStr(desstr=desStr, substr=subStr)
