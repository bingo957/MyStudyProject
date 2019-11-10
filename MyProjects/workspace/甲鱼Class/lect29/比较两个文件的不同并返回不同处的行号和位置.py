"""
比较两个文件的不同，返回不同处的行阿红和位置，如果相同就返回相同字样
"""
# D:\PycharmProjects\PythonProjects\workspace\JiayuClass\lect30\与腾讯20亿合同备忘录.txt
# D:\PycharmProjects\PythonProjects\workspace\JiayuClass\lect30\聊天记录.txt


def files_differ(file1, file2):
    print('=================================i love fishC.com===================================')
    count1 = 0  # 记录行数
    count2 = 0
    global differ_list
    differ_list = list()
    file_1_label = open(file1, 'r')
    file_2_label = open(file2, 'r')
    file_1_content = file_1_label.readlines()
    for file_1_everyline in file_1_content:
        file_2_line = file_2_label.readline()
        count1 += 1
        if file_1_everyline != file_2_line:
            global index
            index = 2
            for i in file_1_everyline:
                count2 += 1
                count3 = 0
                for x in file_2_line:
                    count3 += 1
                    if count2 == count3:
                        if i != x:
                            count4 = file_1_everyline.find(i)
                            differ_list.append((count1, count4))
    file_1_label.close()
    file_2_label.close()


file_1 = input('请输入需要比较的文件路径：')
file_2 = input('请输入需要比较的另一个文件路径：')
index = 1
files_differ(file_1, file_2)
if index == 1:
    print('这两个文件完全相同！')
else:
    print('不同的行号及位置为（行号，位置【从0开始】）：')
    print(differ_list)
print('=================================i love fishC.com===================================')
