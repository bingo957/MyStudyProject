# 按找要求将record.txt中的内容分割并腌制在不同文件下 #
# record.txt文件即上节课中文件 #
import pickle


def file_save(boy, girl, count):
    """将取出的部分文件二进制保存在不同命名的文件，并存储在磁盘上"""
    boy_file_name = 'boy_' + str(count) + '.pkl'
    girl_file_name = 'girl_' + str(count) + '.pkl'
    boy_file = open(boy_file_name, 'wb')
    girl_file = open(girl_file_name, 'wb')
    pickle.dump(boy, boy_file)
    pickle.dump(girl, girl_file)
    boy_file.close()
    girl_file.close()


def file_split(filename):
    f = open(filename)
    boy = []
    girl = []
    count = 1

    for each_line in f:
        if each_line[:6] != '======':
            # 字符串按冒号分割 #
            (name, statement) = each_line.split(':', 1)
            if name == '小甲鱼':
                boy.append(statement)
            else:
                girl.append(statement)

        else:
            file_save(boy, girl, count)
            boy = []
            girl = []
            count += 1
    file_save(boy, girl, count)
    f.close()


# 调用函数 #
file_split(r'D:\PycharmProjects\PythonProjects\workspace\JiayuClass\lect32\record.txt')
