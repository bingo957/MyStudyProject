"""
通讯录程序
"""
import sys
import json


def search_info():
    name = input('请输入联系人姓名：')
    with open(r'D:\PycharmProjects\PythonProjects\workspace\JiayuClass\lect26\contact_data.txt', 'r') as f:
        js = f.read()
        try:
            contact_dict = json.loads(js)
        except json.decoder.JSONDecodeError:
            print('通讯录为空，请先创建！')
            guide()
        else:
            while True:
                try:
                    print(name + '的联系号码为：' + contact_dict[name], end='')
                except KeyError:
                    print('联系人不存在！')
                    name = input('请重新输入（输入rb返回欢迎页）：')
                    if name == 'rb':
                        guide()
                        break
                    else:
                        continue
                else:
                    break
    while True:
        cont_ser = input('是否继续查询 yes/no ：')
        if cont_ser == 'yes':
            search_info()
            break
        elif cont_ser == 'no':
            guide()
            break
        else:
            print('指令错误！')


def creat_new():
    with open(r'D:\PycharmProjects\PythonProjects\workspace\JiayuClass\lect26\contact_data.txt', 'r') as f:
        js = f.read()
    name = input('请输入要添加的联系人姓名：')
    try:
        contact_dict = json.loads(js)
    except json.JSONDecodeError:
        contact_dict = dict()
    else:
        while True:
            if name in contact_dict:
                print('联系人已存在！')
                name = input('请重新输输入（输入ds直接查看该联系人）：')
                if name == 'ds':
                    search_info()
                    break
                else:
                    continue
            else:
                break
    finally:
        while True:
            decide = input('要添加的联系人姓名为：' + name + '  是否确认添加 yes/no ：')
            if decide == 'yes':
                break
            if decide == 'no':
                creat_new()
                break
            else:
                print('指令错误！')
                continue
    info = input('请输入联系人号码：')
    while True:
        decide1 = input('要添加的联系人号码为：' + info + '  是否确认添加 yes/no ：')
        if decide1 == 'yes':
            break
        if decide1 == 'no':
            info = input('请重新输输入联系人号码：')
        else:
            print('指令错误！')
            continue
    contact_dict[name] = info
    js = json.dumps(contact_dict, indent=3)
    with open(r'D:\PycharmProjects\PythonProjects\workspace\JiayuClass\lect26\contact_data.txt', 'w+') as f:
        f.write(js)
    while True:
        cont_add = input('是否继续添加 yes/no ：')
        if cont_add == 'yes':
            creat_new()
            break
        elif cont_add == 'no':
            guide()
            break
        else:
            print('指令错误！')


def delete_info():
    name = input('请输入要删除联系人姓名：')
    with open(r'D:\PycharmProjects\PythonProjects\workspace\JiayuClass\lect26\contact_data.txt', 'r') as f:
        js = f.read()
    try:
        contact_dict = json.loads(js)
    except json.JSONDecodeError:
        print('通讯录为空，不需要删除！')
        guide()
    else:
        while True:
            try:
                decide2 = input('您要删除的联系人为：' + contact_dict[name] + '是否删除（yes/no）')
            except KeyError:
                print('联系人不存在！')
                name = input('请重新输入（输入rb返回欢迎页）：')
                if name == 'rb':
                    guide()
                    break
                else:
                    continue
            else:
                if decide2 == 'yes':
                    contact_dict.pop(name)
                    break
                elif decide2 == 'no':
                    delete_info()
                    break
                else:
                    print('指令错误！')
        js = json.dumps(contact_dict, indent=3)
        with open(r'D:\PycharmProjects\PythonProjects\workspace\JiayuClass\lect26\contact_data.txt', 'w+') as f:
            f.write(js)
    while True:
        cont_del = input('是否继续删除 yes/no ：')
        if cont_del == 'yes':
            delete_info()
            break
        elif cont_del == 'no':
            guide()
            break
        else:
            print('指令错误！')


def guide():
    print('============================')
    print('|--- 欢迎进入通讯录程序 ---|')
    print('|---  1：查询联系人资料 ---|')
    print('|---  2：新建联系人 -------|')
    print('|---  3：删除已有联系人 ---|')
    print('|---  4：退出通讯录程序 ---|')
    print('============================')

    command = int(input('\n请选择输入上方指令代码：'))
    if command in [1, 2, 3, 4]:
        if command == 1:
            search_info()
        elif command == 2:
            creat_new()
        elif command == 3:
            delete_info()
        else:
            sys.exit()
    else:
        print('指令有误，请按照要求输入指令：')
        guide()


if __name__ == '__main__':
    guide()
