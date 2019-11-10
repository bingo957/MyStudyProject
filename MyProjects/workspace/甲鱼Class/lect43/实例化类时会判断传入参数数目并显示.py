class C:
    def __init__(self, *args):
        if not args:
            print('并没有传入参数！')
        else:
            print('传入参数数目为:%d,分别是：' % len(args), end='')
            for i in args:
                print(i, end=',')
