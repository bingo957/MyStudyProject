"""
给之前的猜数字游戏加上图形界面
"""
import random
import easygui as g

msg = '准备好开始我们的小游戏吗？'
title = '猜数字小游戏'
g.msgbox(msg=msg, title=title, ok_button='ready!', image='ready.gif')
number = random.randint(1, 20)
title1 = '-------------------我爱鱼c工作室--------------------'
msg1 = '不妨猜一下我现在想的哪个数字[1~20]：'
guess = g.integerbox(msg=msg1, title=title1, lowerbound=1, upperbound=20, image='num.gif')
i = 1
if guess == number:
    msg2 = '哇草，你是我心里的蛔虫吗？！\n 哼，猜对了也没奖励！'
    title2 = '-------------------我爱鱼c工作室--------------------'
    g.msgbox(msg=msg2, title=title2, ok_button='next', image='excellent.gif')
else:
    while guess != number:
        i = i + 1
        if guess < number:
            msg3 = '嘿，小了，小了！再猜一次吧~'
            title3 = '-------------------我爱鱼c工作室--------------------'
            guess = g.integerbox(msg=msg3, title=title3, lowerbound=1, upperbound=20, image='comeon.gif')
        else:
            msg4 = '哥，大了，大了！再猜一次吧~'
            title4 = '-------------------我爱鱼c工作室--------------------'
            guess = g.integerbox(msg=msg4, title=title4, lowerbound=1, upperbound=20, image='comeon.gif')
    if i < 5:
        msg5 = '还不错，五次以内就猜对了-v-'
        title5 = '-------------------我爱鱼c工作室--------------------'
        g.msgbox(msg=msg5, title=title5, ok_button='next', image='good.gif')
    else:
        msg6 = '终于猜对了，你可急死我了T_T'
        title6 = '-------------------我爱鱼c工作室--------------------'
        g.msgbox(msg=msg6, title=title6, ok_button='next', image='notbad.gif')
msg7 = '游戏结束，不玩了~~~'
title7 = '-------------------我爱鱼c工作室--------------------'
g.msgbox(msg=msg7, title=title7, ok_button='finish', image='bye.gif')
