"""
密码规律：
1、每位密码为单个小写字符
2、每位密码的左右两边均有且只有3个大写字母
"""
with open('string.txt', 'r') as f:
    str1 = f.read().strip('\n')
    count1 = 0
    count2 = 0
    count3 = 0
    length = len(str1)
    for i in range(length):
        if str1[i].isupper():
            if count2 == 1:
                count3 += 1
                count1 = 0
            else:
                count1 += 1
            continue
        if str1[i].islower() and count1 == 3:
            count2 = 1
            count1 = 0
            target = i
            continue
        if str1[i].islower() and count3 == 3:
            print(str1[target], end='')
        count1 = 0
        count2 = 0
        count3 = 0
