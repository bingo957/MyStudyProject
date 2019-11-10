"""
在之前猜数字游戏中加入异常处理机制
"""
import random
import sys


def re_input():
    try:
        global i
        if i == 0:
            temp = input('不妨猜一下我现在想的哪个[1~20]的数字：')
            i = 1
        else:
            temp = input('再猜一次：')
        global guess
        guess = int(temp)
    except ValueError:
        print('输入错误，请输入一个数字！！！')
        re_input()
    except KeyboardInterrupt:  # 不懂为什么CTRL+C停止不了程序？？？？？？
        sys.exit()
    else:
        return guess


print('-------------------我爱鱼c工作室--------------------')
number = random.randint(1, 20)
i = 0
re_input()
if guess == number:
    print('哇草，你是我心里的蛔虫吗？！')
    print('哼，猜对了也没奖励！')
else:
    while guess != number:
        i += 1
        if guess < number:
            print('嘿，小了，小了！')
        else:
            print('哥，大了，大了！')
        re_input()
    if i < 5:
        print('还不错，五次以内就猜对了')
    else:
        print('终于猜对了，你可急死我了')
print('游戏结束，不玩了~~~')
