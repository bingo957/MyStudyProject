"""
猜数字游戏
"""

import random
print('-------------------我爱鱼c工作室--------------------')
number = random.randint(1, 20)
temp = input('不妨猜一下我现在想的哪个数字：')
guess = int(temp)
i = 1
if guess == number:
    print('哇草，你是我心里的蛔虫吗？！')
    print('哼，猜对了也没奖励！')
else:
    while guess != number:
        i = i + 1
        if guess < number:
            print('嘿，小了，小了！')
        else:
            print('哥，大了，大了！')
        temp = input('再猜一次：')
        guess = int(temp)
    if i < 5:
        print('还不错，五次以内就猜对了')
    else:
        print('终于猜对了，你可急死我了')
print('游戏结束，不玩了~~~')
