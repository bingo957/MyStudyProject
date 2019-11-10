"""
统计当前的代码量，并计算距离10万行代码还有多远
要求1：敌对搜索各个文件夹
要求2：显示各类型原文件和源代码数量
要求3：显示总行数于百分比
"""

import easygui as g
import os


def show_result():
    total = 0
    text = ''

    for i in source_list:
        lines = source_list[i]
        total += lines
        text += '【%s】源文件%d个，源代码%d行\n' % (i, file_list[i], lines)
    title = '统计结果'
    msg = '你们目前共编写了%d行代码，完成进度：%.2f %%\n离10万行代码还差%d行，请继续努力！'\
          % (total, total/1000, 100000 - total)
    g.textbox(msg, title, text)


def calc_code(file_name):
    lines = 0
    with open(file_name) as f:
        print('正在分析文件：%s...' % file_name)  # 这里可以改为用gui显示
        try:
            for each_line in f:
                each_line += ''  # 无任何作用
                lines += 1
        except UnicodeDecodeError:
            pass  # 格式不兼容文件忽略掉
    return lines


def search_file(start_dir):
    os.chdir(start_dir)

    for each_file in os.listdir(os.curdir):
        ext = os.path.splitext(each_file)[1]
        if ext in target:
            lines = calc_code(each_file)  # 统计行数
            # 字典中不存在，抛出KeyError，添加字典键
            # 统计文件数
            try:
                file_list[ext] += 1
            except KeyError:
                file_list[ext] = 1
            # 统计源代码行数
            try:
                source_list[ext] += lines
            except KeyError:
                source_list[ext] = lines

        if os.path.isdir(each_file):
            search_file(each_file)  # 递归调用
            os.chdir(os.pardir)  # 返回上一层目录


target = ['.c', '.cpp', '.py', '.cc', '.java', '.pas', '.asm']
file_list = {}
source_list = {}

g.msgbox('请打开您存放所有代码的文件夹...', '统计代码量')
path = g.diropenbox('请选择您的代码库：')

if __name__ == '__main__':
    search_file(path)
    show_result()
