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
import numpy as np
import os
import xlwings as xw
import shutil


def del_outlier(file_load):
    """
    此程序功能为：将参数汇总处理中的要用数据提取出来，将离群值去掉后保存在新建的《去离群值参数汇总.xlsx》中
       去离群值原理：
                    111
    """
    select_data = ['vth定(+)', 'vth截(+)', 'ion(+)']
    cycle_num = [3, 6, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    cell_mark = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
    os.chdir(file_load + '\\数据处理')
    shutil.copy(file_load + '\\其它模板\\去离群值参数汇总x2.xlsx', os.curdir)
    app = xw.App(visible=True, add_book=True)
    app.display_alerts = True
    app.screen_updating = True
    wb = app.books.open('去离群值参数汇总x2.xlsx')
    for every_select_data in select_data:
        a = 0
        for i in cycle_num:
            excel_data = pd.read_excel(os.curdir + '\\参数汇总处理.xlsx', sheet_name='%s' % every_select_data, usecols=[a],
                                       header=0, error_bad_lines=False)
            list_df = excel_data.values.tolist()
            data_list1 = []
            for every_list_df in list_df:
                if every_list_df[0] == every_list_df[0]:
                    data_list1.append(every_list_df[0])
            deerta_sifenwei = (np.percentile(data_list1, 75, interpolation='lower') - np.percentile(data_list1, 25, interpolation='higher')) * 2
            data_max = np.percentile(data_list1, 75, interpolation='lower') + deerta_sifenwei
            data_min = np.percentile(data_list1, 25, interpolation='higher') - deerta_sifenwei
            data_list2 = ['%dK' % i]
            for every_data_list in data_list1:
                if every_data_list <= data_max:
                    if every_data_list >= data_min:
                        data_list2.append(every_data_list)
            sheet = wb.sheets[every_select_data]
            sheet.range('%s1' % cell_mark[a]).options(transpose=True).value = data_list2
            a += 1
    wb.save()
    wb.close()
    app.quit()


if __name__ == '__main__':
    topfile = input('请给出顶层文件夹路径：')
    del_outlier(topfile)
