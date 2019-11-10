# 计算路径下所有文件的大小 结果返回 bytes 形式 #


import os


def file_folder_cal(path):
    size = 0
    for root, dirs, files in os.walk(path):
        for name in files:
            size += os.path.getsize(os.path.join(root, name))
    return size


def file_cal(path):
    all_file = os.listdir(path)
    file_dict = dict()

    for every_file in all_file:
        if os.path.isdir(os.path.join(path, every_file)) is True:
            file_dict.setdefault(every_file, 0)
            file_dict[every_file] = file_folder_cal(os.path.join(path, every_file))
        else:
            file_dict.setdefault(every_file, 0)
            file_dict[every_file] = os.path.getsize(every_file)

    for every_key in file_dict.keys():
        print(every_key + ':' + str(file_dict[every_key]) + 'Bytes')


file_cal(r'D:\音乐\杰伦合集')
