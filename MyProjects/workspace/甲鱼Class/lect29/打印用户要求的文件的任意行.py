"""
用户随意输入需要显示的行数，然后打印这些行数
"""


def print_requirements(file_name, num1, num2):
    print('=================================i love fishC.com===================================')
    print('\n%s    文件的 %d~%d 行为：\n' % (file_name, num1, num2))
    f = open(file_name, 'r')
    count = 0
    for each_line in f.readlines():
        count += 1
        if num1 <= count <= num2:
            print(each_line, end='')
    f.close()
    print('\n===================================Program End=====================================')


file_load = input('请输入要打开文件的路径：')
(number1, number2) = input('请输入打印行数,格式为【 1-2 】:').split('-', 1)
print_requirements(file_load, int(number1), int(number2))
