"""
根据需要，将文件中的字符或字符串全体换为需要的内容
"""
# D:\PycharmProjects\PythonProjects\workspace\JiayuClass\lect30\聊天记录.txt


def file_replace(file_name, rep_word, new_word):
    print('=================================i love fishC.com===================================')
    file_read = open(file_name, 'r')
    count = 0
    content = []
    for each_line in file_read.readlines():
        if rep_word in each_line:
            count += each_line.count(rep_word)
            each_line = each_line.replace(rep_word, new_word)
        content.append(each_line)
    decide = input('\n文件中共有%d个【%s】\n您确定要把所有的【%s】替换为【%s】吗？\n【yes/no】:' % (count, rep_word,
                                                                         rep_word, new_word))
    if decide in ['YES', 'Yes', 'yes']:
        file_write = open(file_name, 'w')
        file_write.writelines(content)
        print('替换完成！')
        file_write.close()
    file_read.close()


file_load = input('请输入要打开文件的路径：')
(word1, word2) = input('请输入被替换词和替换词,格式为【 old-new 】:').split('-', 1)
file_replace(file_load, word1, word2)
print('\n===================================Program End=====================================')
