#
#                 God Bless No Bugs!
#
#                       _ooOoo_
#                      o8888888o
#                      88" . "88
#                      (| -_- |)
#                      O\  =  /O
#                   ____/`---'\____
#                 .'  \\|     |//  `.
#                /  \\|||  :  |||//  \
#               /  _||||| -:- |||||-  \
#               |   | \\\  -  /// |   |
#               | \_|  ''\---/''  |   |
#               \  .-\__  `-`  ___/-. /
#             ___`. .'  /--.--\  `. . __
#          ."" '<  `.___\_<|>_/___.'  >'"".
#         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#         \  \ `-.   \_ __\ /__ _/   .-` /  /
#    ======`-.____`-.___\_____/___.-`____.-'======
#                       `=---='
#    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#
# coding: utf-8 #
#  author:李斌  #


class MyDes:
    """
    此描述符作用为对属性做出操作时自动提醒
    """
    def __int__(self, value=None, name=None):
        self.val = value
        self.name = name

    def __get__(self, instance, owner):
        print('正在获取变量：', self.name)
        return self.val

    def __set__(self, instance, value):
        print('正在修改变量:', self.name)
        self.val = value

    def __delete__(self, instance):
        print('正在删除变量：', self.name)
        print('此变量无法删除！')
