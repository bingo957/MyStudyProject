# 在输入目录下搜索视频文件，并将文件路径保存在一个 .txt 文件中 #

import os
index = 1


def file_search(path, file_type):
    os.chdir(path)

    for every_file in os.listdir(os.curdir):
        f = os.path.splitext(os.path.join(os.curdir, every_file))[1]
        if f in file_type:
            global video_list
            video_list = open(r'D:\PycharmProjects\PythonProjects\workspace\JiayuClass\lect31\videolist.txt', 'a')
            video_list.writelines(os.getcwd() + os.sep + every_file + '\n')
            global index
            index = 2
        if os.path.isdir(os.path.join(os.curdir, every_file)):
            file_search(os.path.join(os.curdir, every_file), file_type)
            os.chdir(os.pardir)


start_dir = input('请输入初始搜索目录：')
target = ['.avi', 'mp4', 'rmvb']
file_search(start_dir, target)
if index == 1:
    print('\n未找到视频文件！')
video_list.writelines('===============================================================================================')
video_list.close()
