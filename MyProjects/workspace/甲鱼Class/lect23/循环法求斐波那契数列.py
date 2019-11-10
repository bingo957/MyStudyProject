def fab(n):
    n1 = 1
    n2 = 1
    n3 = 1

    if n == 1 or n == 2:
        return 1
    else:
        while (n - 2) > 0:
            n3 = n1 + n2
            n1 = n2
            n2 = n3
            n -= 1
        return n3

n = int(input('请输入您想获取数列的级数：'))
alist = []

if n < 1 :
    print('输入有误，输入的数必须为正整数！')
else:
    while (n > 0):
        result = fab(n)
        alist.append(result)
        n -= 1
    n += 1
    
if n == 1:
    alist.reverse()
    for num in alist:
        print(num,end = ' ')
