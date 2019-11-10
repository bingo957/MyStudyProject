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

import pandas as pd
import os
import xlwings as xw


def split(file_load):
    """
    此程序功能为：将参数汇总处理中的要用数据提取出来，将离群值去掉后保存在新建的《去离群值参数汇总.xlsx》中
       去离群值原理：
                    111
    """
    cycle_num = [3, 6, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    cell_mark = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
    os.chdir(file_load + '\\数据处理')
    app = xw.App(visible=True, add_book=True)
    app.display_alerts = True
    app.screen_updating = True
    wb = app.books.add()
    wb.sheets.add('ion-大')
    wb.sheets.add('ion-小')
    a = 0
    for i in cycle_num:
        excel_data = pd.read_excel(os.curdir + '\\参数汇总处理.xlsx', sheet_name='ion(+)', usecols=[a],
                                   header=0, error_bad_lines=False)
        list_df = excel_data.values.tolist()
        data_list_init = []
        for every_list_df in list_df:
            if every_list_df[0] == every_list_df[0]:
                data_list_init.append(every_list_df[0])
        data_list1 = ['%dK' % i]
        data_list2 = ['%dK' % i]
        for every_data_list in data_list_init:
            if every_data_list <= 0.05:
                data_list1.append(every_data_list)
            else:
                data_list2.append(every_data_list)
        sheet1 = wb.sheets['ion-小']
        sheet2 = wb.sheets['ion-大']
        sheet1.range('%s1' % cell_mark[a]).options(transpose=True).value = data_list1
        sheet2.range('%s1' % cell_mark[a]).options(transpose=True).value = data_list2
        a += 1
    wb.save('大-小退化分离.xlsx')
    wb.close()
    app.quit()


if __name__ == '__main__':
    topfile = input('请给出顶层文件夹路径：')
    split(topfile)

# 仅处理112#/113#-0.1v
