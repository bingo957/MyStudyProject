"""
文件夹浏览框，让用户选择并打开需要的文本文件，并显示文件内容
"""

import easygui as g
import os
import sys

file_path = g.fileopenbox(default=r'D:\PycharmProjects\PythonProjects\workspace\JiayuClass')

try:
    with open(file_path, 'r') as f:
        title = os.path.basename(file_path)
        msg = '文件【%s】的内容如下' % title
        text = f.read()
        g.textbox(msg, title, text)
except TypeError:
    sys.exit()
