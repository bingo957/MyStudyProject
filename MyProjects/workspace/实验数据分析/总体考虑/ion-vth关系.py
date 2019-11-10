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


def ion_vs_vth(file_load):
    """
    此程序功能为：将参数汇总处理中的要用数据提取出来，将离群值去掉后保存在新建的《去离群值参数汇总.xlsx》中
       去离群值原理：
                    111
    """
    cycle_num = [3, 6, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    cell_mark = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'u', 'v', 'w', 'x']
    os.chdir(file_load + '\\数据处理')
    app = xw.App(visible=True, add_book=True)
    app.display_alerts = True
    app.screen_updating = True
    wb = app.books.add()
    wb.sheets.add('ion-vth关系')
    a = 1
    c = 0
    for i in cycle_num:
        print('请注意下方输入时必须输入英文字符！！！')
        error_ifo = input('请输入%dK异常器件标号（格式：1.12,2.10,3.12）：' % i)  # 注意输入法必须是英文
        if error_ifo == '':
            error_dev = []
        else:
            error_dev = error_ifo.split(',')
        error_list = []
        for each_error in error_dev:
            if each_error.split('.', 1)[0] == '1':
                error_list.append(int(each_error.split('.', 1)[1]))
            elif each_error.split('.', 1)[0] == '2':
                error_list.append(int(each_error.split('.', 1)[1]) + 28)
            else:
                error_list.append(int(each_error.split('.', 1)[1]) + 56)
        error_list.sort(reverse=True)
        excel_data_for_num_vth = pd.read_excel(os.curdir + '\\参数汇总处理.xlsx', sheet_name='vth截', usecols=[a + 1], header=0,
                                               error_bad_lines=False)
        list_df_vth = excel_data_for_num_vth.values.tolist()
        excel_data_for_num_ion = pd.read_excel(os.curdir + '\\参数汇总处理.xlsx', sheet_name='ion', usecols=[a], header=0,
                                               error_bad_lines=False)
        list_df_ion = excel_data_for_num_ion.values.tolist()
        for every_error_list in error_list:
            del list_df_ion[every_error_list - 1]
            del list_df_vth[every_error_list - 1]
        data_list_ion = ['%dK' % i]
        data_list_vth = ['%dK' % i]
        for b in range(len(list_df_ion)):
            if list_df_vth[b][0] >= 0:
                if list_df_ion[b][0] >= 0:
                    data_list_ion.append(list_df_ion[b][0])
                    data_list_vth.append(list_df_vth[b][0])
        sheet = wb.sheets['ion-vth关系']
        sheet.range('%s1' % cell_mark[c]).options(transpose=True).value = data_list_ion
        sheet.range('%s1' % cell_mark[c + 1]).options(transpose=True).value = data_list_vth
        a += 2
        c += 2
    wb.save('ion-vth关系.xlsx')
    wb.close()
    app.quit()


if __name__ == '__main__':
    topfile = input('请给出顶层文件夹路径：')
    ion_vs_vth(topfile)

# 113/ 1.4,1.12,1.20,1.21,1.28,2.10,2.11,2.12,2.17,2.18,2.20,2.24,2.28,3.3,3.6,3.8,3.15,3.21,3.22,3.23,3.24
# 112/ 1.3,1.19,2.8,2.20,3.2,3.13
