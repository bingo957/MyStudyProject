# 文件按要求切割并保存 #


def file_save(boy, girl, count):
    """将指定部分文件保存在创建好的文件内"""
    boy_file_name = 'boy_' + str(count) + '.txt'
    girl_file_name = 'girl_' + str(count) + '.txt'
    boy_file = open(boy_file_name, 'w')
    girl_file = open(girl_file_name, 'w')
    # 指定不存在文件创建路径方法
    # 不指定时，默认路径为用 open（）方法打开的文件的同层路径
    # boy_file = open(r'D:\PycharmProjects\PythonProjects\workspace\JiayuClass\lect30\boy_' + boy_file_name, 'w')
    # girl_file = open(r'D:\PycharmProjects\PythonProjects\workspace\JiayuClass\lect30\girl_' + girl_file_name, 'w')
    boy_file.writelines(boy)
    girl_file.writelines(girl)
    boy_file.close()
    girl_file.close()
    girl_file.close()


def file_split(file_name):
    """将文件按要求分割"""
    f = open(file_name)
    boy = []
    girl = []
    count = 1
    for each_line in f:
        if each_line[:6] != '======':
            # 字符串按冒号分割
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
file_split(r'D:\PycharmProjects\PythonProjects\workspace\JiayuClass\lect30\聊天记录.txt')
