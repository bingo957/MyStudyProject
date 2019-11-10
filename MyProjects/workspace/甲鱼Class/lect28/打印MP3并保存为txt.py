"""
打印MP3会发生什恶魔？
"""
f = open(r'D:\音乐\杰伦合集\Jay\周杰伦 - 斗牛.mp3')
for every_line in f:
    f_content = f.read()
    print(every_line, end='')
f2 = open(r'D:\PycharmProjects\PythonProjects\workspace\JiayuClass\lect29\斗牛.txt', 'x')
f2.write(f_content)
f.close()
f2.close()
