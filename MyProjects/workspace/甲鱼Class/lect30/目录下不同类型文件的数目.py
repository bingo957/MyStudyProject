# 返回指定目录下不同类型文件的数目 #
# 该方法的结果证明 os.walk（）方法会遍历top路径下所有的文件以及文件中的子文件一直到最底层 #


import os
import os.path


def file_num(top):
    count = 0
    count_txt = 0
    count_png = 0
    count_py = 0
    count_docx = 0
    count_other = 0
    for (root, dirs, files) in os.walk(top, topdown=False):
        for every_dirs in dirs:
            count += 1
        for every_file in files:
            (file_name, file_extension) = os.path.splitext(every_file)
            if file_extension == '.txt':
                count_txt += 1
            elif file_extension == '.png':
                count_png += 1
            elif file_extension == '.py':
                count_py += 1
            elif file_extension == '.docx':
                count_docx += 1
            else:
                count_other += 1
    print('目录中的文件夹个数为：%d个' % count)
    print('目录中的[txt]文件个数为：%d个' % count_txt)
    print('目录中的[xlsx]文件个数为：%d个' % count_png)
    print('目录中的[py]文件个数为：%d个' % count_py)
    print('目录中的[docx]文件夹个数为：%d个' % count_docx)
    print('目录中的其它文件个数为：%d个' % count_other)


file_num(r'D:\Administrator\桌面')
