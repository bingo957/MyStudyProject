def factorial(n):
    '递归法求阶乘'
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)

number = int(input('请输入一个非负整数：'))
result = factorial(number)
print('%d 的阶乘是 %d' % (number,result))
