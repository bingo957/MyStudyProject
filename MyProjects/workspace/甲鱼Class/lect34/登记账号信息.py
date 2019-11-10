"""
实现一个用于登记用户账号信息的界面（带*必填，且不能是空格）
"""
import easygui as g
import sys

text = ['\n']
msg = '请输入以下信息，带*为必填项且不能只有空格'
title = '鱼c工作室账号中心'
field_names = ['*用户名', '*真实姓名', '固定电话', '*手机号码', 'QQ', '*E-mail']
field_values = g.multenterbox(msg=msg, title=title, fields=field_names)
while True:
    a = 0
    if field_values is None:
        break
    for i in range(len(field_names)):
        if field_values[i].strip() == '':
            a += 1
    if a == 6:
        msg1 = '请注意格式正确输入（不能为空或空格）'
        title1 = 'Warning!!!'
        field_values = g.multenterbox(msg=msg1, title=title1, fields=field_names)
        continue
    er_msg = ''
    for i in range(len(field_names)):
        option = field_names[i].strip()
        if field_values[i].strip() == '' and option[0] == '*':
            er_msg += '[%s]是必填项。\n' % field_names[i]
    if er_msg != '':
        title2 = 'Warning!!!'
        field_values = g.multenterbox(msg=er_msg, title=title2, fields=field_names)
        continue
    else:
        for i in range(len(field_names)):
            if field_values[i].strip() != '':
                text.append(field_names[i].strip('*') + ' : ' + field_values[i].strip() + '\n\n')
        break
if text[0] != '\n':
    title3 = '鱼c工作室账号中心'
    msg3 = '用户资料如下：'
    g.textbox(msg=msg3, title=title3, text=text)
else:
    sys.exit()
