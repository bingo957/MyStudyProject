# 用户输入关键字，查找指定文件夹内所有含有该关键字的文本文档 #
# 显示文本文档的路径并显示关键字坐标 #

import os
index = 1


def word_location(path, keyword):
    """找到文件下的关键字"""
    loc = 1
    f = open(path, encoding='gb18030', errors='ignore')
    lines = f.readlines()
    for every_line in lines:
        pos = every_line.find(keyword)
        if pos != -1:
            global index
            index = 2
            print('路径:' + os.getcwd() + path.split('.', 1)[1] + '\n')
            print('位置【行号；坐标】：【%d ; %d】' % (loc, pos))
            print('================================================================================================')
        loc += 1
    f.close()


def search_txt(path, keyword):
    """寻找 .TXT 格式文件"""
    os.chdir(path)

    for every_file in os.listdir(os.curdir):
        f = os.path.splitext(os.path.join(os.curdir, every_file))[1]
        if f == '.txt':
            word_location(os.path.join(os.curdir, every_file), keyword)
        if os.path.isdir(os.path.join(os.curdir, every_file)) is True:
            search_txt(os.path.join(os.curdir, every_file), keyword)
            os.chdir(os.pardir)


start_dir = input('请输入初始搜索目录：')  # D:\Administrator\桌面
target = input('请输入要搜索的关键字：')  # python
print('=======================================I love FishC.com==========================================')
search_txt(start_dir, target)
if index == 1:
    print('\n未找到该关键词！')
    print('=================================================================================================')
