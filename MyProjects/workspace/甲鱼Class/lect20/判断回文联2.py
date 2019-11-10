# 方法二
def palindrome(string):
   list1 = list(string)
   list2 = reversed(list1)
   if list1 == list(list2):
       print('是回文联！')
   else:
       print('不是回文联！')


palindrome(input('请输入一句话：'))
