"""
只能输入整数，否则重新输入
"""


def int_input(prompt):
    try:
        int_num = int(prompt)
    except ValueError:
        print('输入错误，您输入的不是一个整数！')
        re_input = input('请重新输入：')
        int_input(re_input)
    else:
        return int_num


prompt_input = input('请输入一个整数：')
int_input(prompt_input)
