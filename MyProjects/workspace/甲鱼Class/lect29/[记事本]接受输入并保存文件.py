"""
接收用户输入并保存为用户命名的文件
"""
import os


def note_book():
    print('=================================i love fishC.com===================================')
    print('【1】已存在的记事本文件有：')
    rf_1 = open(r'D:\PycharmProjects\PythonProjects\workspace\JiayuClass\lect30\record_file.txt', 'r')
    lines = rf_1.readlines()
    for every_line in lines:
        print(every_line, end=' ')
        rf_1.close()
    print('\n')
    res = input('【2】请查看已经存在的文件并决定是否创建新文件(yes or no),请输入【y/n】：')
    if res == 'y':
        name = input('【3】请输入新建文件名：')
        rf_2 = open(r'D:\PycharmProjects\PythonProjects\workspace\JiayuClass\lect30\record_file.txt', 'x')
        rf_2.write('《' + name + '》')
        rf_2.close()
    else:
        name = input('【3】请输入要打开的文件名：')
    f = open(r'D:\PycharmProjects\PythonProjects\workspace\JiayuClass\lect30' + os.sep + name + '.txt', 'a')
    while True:
        file_content = input('【4】请输入文件内容，当输入’ ;w ‘时结束程序输入并保存:')
        if file_content != ';w':
            f.writelines('%s\n' % file_content)
        else:
            break
    f.close()
    print('=================================i love fishC.com===================================')


note_book()
