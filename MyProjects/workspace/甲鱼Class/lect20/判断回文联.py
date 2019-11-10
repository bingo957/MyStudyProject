"""
例：上海自来水来自海上
"""
def palindrome(string):
    length = len(string)
    last = length - 1
    length //= 2
    flag = 1
    for i in range(length):
        if string[i] != string[last]:
            flag = 0
            break
        last -= 1

    if flag == 1:
        return  1
    else:
        return  0


string1 = input("请输入一句话：")
if palindrome(string1) == 1:
    print('是回文联！')
else:
    print('不是回文联！')
