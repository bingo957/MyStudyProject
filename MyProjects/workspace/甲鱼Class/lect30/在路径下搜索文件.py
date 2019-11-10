# 在路径下搜索文件，当遇到文件夹时进入文件夹搜索 #

import os
index = 1


def file_search(path, name):
    os.chdir(path)

    for every_file in os.listdir(os.curdir):
        if every_file == name:
            print('\n要搜索的文件位置为：' + os.getcwd() + os.sep + every_file)
            global index
            index = 2
        if os.path.isdir(os.path.join(os.curdir, every_file)) is True:
            file_search(os.path.join(os.curdir, every_file), name)
            os.chdir(os.pardir)


start_dir = input('请输入初始搜索目录：')
target = input('请输入要搜索的文件：')
file_search(start_dir, target)
if index == 1:
    print('\n未找到该文件！')
