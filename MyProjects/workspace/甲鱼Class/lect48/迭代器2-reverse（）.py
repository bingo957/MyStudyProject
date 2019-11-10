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


class MyDev:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]
