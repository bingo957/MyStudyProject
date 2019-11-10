# 返回指定目录下不同类型文件的数目 #


import os


def file_num(path):
    all_file = os.listdir(path)
    file_dict = dict()

    for every_file in all_file:
        if os.path.isdir(os.path.join(path, every_file)) is True:
            file_dict.setdefault('文件夹', 0)
            file_dict['文件夹'] += 1
        else:
            extension = os.path.splitext(every_file)[1]
            file_dict.setdefault(extension, 0)
            file_dict[extension] += 1
    for every_type in file_dict.keys():
        print('此目录下有【%s】类型的文件 %d 个' % (every_type, file_dict[every_type]))


file_num(r'D:\Administrator\桌面')