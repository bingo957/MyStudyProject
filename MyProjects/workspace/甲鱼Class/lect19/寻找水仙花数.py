"""
寻找水仙花数
要求：如果一个3位数等于其各位数宇的立方和，则称这个数为水仙花数。
例如153=1^3+5^3+3^3,因此153是一个水仙花数。
编写一个程序，找出所有的水仙花数。
"""


def findNarcissus():
    for each in range(100, 1000):
        sum = (each//100)**3 + ((each-(each//100*100))//10)**3 +\
              (each - ((each//100)*100)-((each-(each//100*100))//10*10))**3
        if sum == each:
            print(each, end=' ')


print('所有的水仙花数是：')
findNarcissus()
