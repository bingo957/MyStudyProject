"""
用户登陆程序
"""
import sys


def new_user(user_data):
    prompt = input('\n请输入用户名：')
    if prompt in user_data:
        chosen = input('用户名已存在,直接登陆请输入 e/E ,重新输入请输入 r/R :')
        if chosen in 'eE':
            show_menu()
        else:
            new_user(user_data)
    else:
        password1 = input('请输入密码：')
        password2 = input('请确认密码：')
        jud = False
        while True:
            if password1 == password2:
                print('注册成功，请重新登录^v^')
                data_file = open(r'D:\PycharmProjects\PythonProjects\workspace\JiayuClass\lect27\user_data.txt', 'a')
                data_file.writelines(prompt + ':' + password1)
                data_file.close()
                jud = True
                break
            else:
                print('两次输入不一致，请重新输入！')
                password1 = input('请输入密码：')
                password2 = input('请确认密码：')
                continue
        if jud is True:
            show_menu()


def old_user(user_data):
    prompt = input('\n请输入用户名：')
    while True:
        if prompt not in user_data:
            prompt = input('您输入的用户名不存在请重新输入【输入 _b_ 回到开始菜单】：')
            if prompt == '_b_':
                break
            else:
                continue
        else:
            break
    if prompt == '_b_':
        show_menu()

    i = 1
    password = input('请输入密码：')
    pwd = user_data.get(prompt)
    while True:
        if password == pwd:
            print('欢迎登陆xxoo系统^v^')
            break
        else:
            if i <= 2:
                print('密码错误，请重新输入：', end='')
                password = input()
                i += 1
            else:
                print(r'错误次数超过限制，找回密码请登录：http:\\www.ilovefishc.com\find_password')
                break
    sys.exit()


def show_menu():
    prompt = '''
     ***** fishC.com *****
    =======================
    |--- 新建用户：N/n ---|
    |--- 登陆账户：E/e ---|
    |--- 退出程序：Q/q ---|
    |--- 请输入指令代码：
 '''
    chosen = False
    choice = input(prompt)
    while not chosen:
        if choice not in 'NnEeQq':
            choice = input('指令输入错误，请重新输入：')
        else:
            chosen = True

    if choice == 'Q' or choice == 'q':
        sys.exit()
    if choice == 'N' or choice == 'n':
        user_data = {}
        new_user(user_data)
    if choice == 'E' or choice == 'e':
        try:
            data_file = open(r'D:\PycharmProjects\PythonProjects\workspace\JiayuClass\lect27\user_data.txt', 'r')
        except FileNotFoundError:
            print('还没有任何用户信息,请新建或退出！')
            show_menu()
        else:
            user_data = {}
            lines = data_file.readlines()
            for each_line in lines:
                user_data[each_line.split(':', 1)[0]] = each_line.split(':', 1)[1].strip('\n')
            old_user(user_data)


if __name__ == '__main__':
    show_menu()
