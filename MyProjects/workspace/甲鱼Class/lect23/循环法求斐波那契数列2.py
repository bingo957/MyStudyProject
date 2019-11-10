n1 = 1
n2 = 1
n3 = 1
n = int(input('请输入您想获取数列的级数：'))

if n < 1:
    print('输入有误，输入的数必须为正整数！')
elif n == 1:
    print(1)
elif n == 2:
    print(1, 1)
else:
    print(1, 1, end=(' '))
    while (n - 2) > 0:
        n3 = n1 + n2
        print(n3, end=(' '))
        n1 = n2
        n2 = n3
        n -= 1
