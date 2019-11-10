"""
文件夹浏览框，让用户选择并打开需要的文本文件，并显示文件内容，当用户点击OK时，检查文本的改变，并让用户选择
如何让处理改变
"""

import easygui as g
import os
import sys

file_path = g.fileopenbox(default=r'D:\PycharmProjects\PythonProjects\workspace\JiayuClass')

try:
    with open(file_path, 'r') as old_file:
        title = os.path.basename(file_path)
        msg = '文件【%s】的内容如下' % title
        text = old_file.read()
        after_text = g.textbox(msg, title, text)
except TypeError:
    sys.exit()
else:
    if text != after_text[:-1]:
        msg1 = '检测到文件内容发生变化，请选择以下操作：'
        title1 = '警告！'
        choice1 = ('覆盖保存', '放弃修改', '另存为')
        choice = g.buttonbox(msg=msg1, title=title1, choices=choice1)
        if choice == '覆盖保存':
            with open(file_path, 'w') as old_file:
                old_file.write(after_text[:])
        if choice == '放弃修改':
            pass
        if choice == '另存为':
            another_path = g.filesavebox(title='另存为', default=r'D:\PycharmProjects\PythonProjects\workspace'
                                                              r'\JiayuClass\.txt')
            if os.path.splitext(another_path)[1] != '.txt':
                another_path += '.txt'
            with open(another_path, 'w') as new_file:
                new_file.write(after_text[:])
