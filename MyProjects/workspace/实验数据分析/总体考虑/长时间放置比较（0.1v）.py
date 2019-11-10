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
import shutil
import xlwings as xw


def lgtCont(file_load):
    """
    此函数功能为：将初始数据插入到后3-纵向对比模板中
    """
    # 设置循环参数
    cycle_num = [0, 80, 90, 100, 200]
    file_flag = ['1.1', '1.2', '1.3', '2.1', '2.2', '2.3', '3.1', '3.2', '3.3', '1.5', '2.7', '2.8', '3.27', '3.28',
                 '1.12', '2.10', '3.6', '1.19', '1.20', '1.21', '2.20', '2.28', '3.22', '3.23']
    cell_num = ['C', 'D', 'G', 'H', 'K', 'L', 'O', 'P', 'S', 'T']
    app = xw.App(visible=True, add_book=False)
    app.display_alerts = True
    app.screen_updating = True
    # 将模板复制进《数据处理》文件夹
    os.chdir(file_load + '\\数据处理')
    shutil.copy(file_load + '\\其它模板\\长时间放置纵向对比.xlsx', os.curdir)
    os.chdir(file_load)
    a = 0
    for i in cycle_num:
        wb = app.books.open(os.curdir + '\\数据处理\\长时间放置纵向对比.xlsx')
        # 从 csv 文件中提取文件并插入到模板中
        if i != 200:
            for each in file_flag:
                os.chdir(os.curdir + '\\原始数据\\%dK' % i)
                sheetnum = each.replace('.', '-')
                # usecols 参数4、5分别为B1500输出csv文件中IG、ID所在列
                csv_data1 = pd.read_csv(os.curdir + '\\%s.csv' % each, usecols=[3], header=682, error_bad_lines=False)
                list1 = csv_data1.values.tolist()
                ig_list = []
                for each_ig in list1:
                    ig_list.append(each_ig[0])
                csv_data2 = pd.read_csv(os.curdir + '\\%s.csv' % each, usecols=[4], header=682, error_bad_lines=False)
                list2 = csv_data2.values.tolist()
                id_list = []
                for each_id in list2:
                    id_list.append(each_id[0])
                os.chdir(file_load)
                sheet1 = wb.sheets['%s' % sheetnum]
                sheet1.range(cell_num[a] + '2').options(transpose=True).value = ig_list
                sheet1.range(cell_num[a + 1] + '2').options(transpose=True).value = id_list
        else:
            for each in file_flag:
                os.chdir(os.curdir + '\\113#长时间放置重测19.10.22')
                sheetnum = each.replace('.', '-')
                # usecols 参数4、5分别为B1500输出csv文件中IG、ID所在列
                csv_data1 = pd.read_csv(os.curdir + '\\%s.csv' % each, usecols=[3], header=682, error_bad_lines=False)
                list1 = csv_data1.values.tolist()
                ig_list = []
                for each_ig in list1:
                    ig_list.append(each_ig[0])
                csv_data2 = pd.read_csv(os.curdir + '\\%s.csv' % each, usecols=[4], header=682, error_bad_lines=False)
                list2 = csv_data2.values.tolist()
                id_list = []
                for each_id in list2:
                    id_list.append(each_id[0])
                os.chdir(file_load)
                sheet1 = wb.sheets['%s' % sheetnum]
                sheet1.range(cell_num[a] + '2').options(transpose=True).value = ig_list
                sheet1.range(cell_num[a + 1] + '2').options(transpose=True).value = id_list
        wb.save()
        wb.close()
        a += 2
        print('%dk数据已经全部提取并插入到长时间放置纵向对比模板中！！！' % i)


if __name__ == '__main__':
    topfile = input('请给出顶层文件夹路径：')
    lgtCont(topfile)
