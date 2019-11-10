"""
打印用户要求的文件的前几行
"""


def print_requirements(file_name, line_num):
    print('=================================i love fishC.com===================================')
    print('%s 文件的前%d行为：' % (file_name, line_num))
    f = open(file_name, 'r')
    for i in range(line_num):
        print(f.readline(), end='')
    f.close()
    print('=================================i love fishC.com===================================')


file_load = input('请输入要打开文件的路径：')
number = int(input('请输入打印行数：'))
print_requirements(file_load, number)
