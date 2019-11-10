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
    cycle_num = [0, 80, 90, 100]
    file_flag1 = ['1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '1.8', '1.9', '1.10', '1.11', '1.12', '1.13',
                  '1.14', '1.15', '1.16', '1.17', '1.18', '1.19', '1.20', '1.21', '1.22', '1.23', '1.24',
                  '1.25', '1.26', '1.27', '1.28']
    file_flag2 = ['2.1', '2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '2.9', '2.10', '2.11', '2.12', '2.13',
                  '2.14', '2.15', '2.16', '2.17', '2.18', '2.19', '2.20', '2.21', '2.22', '2.23', '2.24',
                  '2.25', '2.26', '2.27', '2.28']
    file_flag3 = ['3.1', '3.2', '3.3', '3.4', '3.5', '3.6', '3.7', '3.8', '3.9', '3.10', '3.11', '3.12', '3.13',
                  '3.14', '3.15', '3.16', '3.17', '3.18', '3.19', '3.20', '3.21', '3.22', '3.23', '3.24',
                  '3.25', '3.26', '3.27', '3.28']
    cell_num = ['C', 'D', 'G', 'H', 'K', 'L', 'O', 'P']
    app = xw.App(visible=True, add_book=False)
    app.display_alerts = False
    app.screen_updating = True
    # 将模板复制进《数据处理》文件夹
    os.chdir(file_load + '\\数据处理')
    shutil.copy(file_load + '\\其它模板\\后3-纵向对比1.xlsx', os.curdir)
    shutil.copy(file_load + '\\其它模板\\后3-纵向对比2.xlsx', os.curdir)
    shutil.copy(file_load + '\\其它模板\\后3-纵向对比3.xlsx', os.curdir)
    os.chdir(file_load)
    a = 0
    for i in cycle_num:
        # 从 csv 文件中提取文件并插入到模板中
        # 操作第一行器件数据
        wb = app.books.open(os.curdir + '\\数据处理\\后3-纵向对比1.xlsx')
        for each in file_flag1:
            os.chdir(os.curdir + '\\原始数据\\%dK' % i)
            sheetnum = each.split('.', 1)[1]
            # usecols 参数4、5分别为B1500输出csv文件中IG、ID所在列
            csv_data1 = pd.read_csv(os.curdir + '\\%s.csv' % each, usecols=[3], header=215, nrows=251, error_bad_lines=False)
            list1 = csv_data1.values.tolist()
            ig_list = []
            for each_ig in list1:
                ig_list.append(each_ig[0])
            csv_data2 = pd.read_csv(os.curdir + '\\%s.csv' % each, usecols=[4], header=215, nrows=251, error_bad_lines=False)
            list2 = csv_data2.values.tolist()
            id_list = []
            for each_id in list2:
                id_list.append(each_id[0])
            os.chdir(file_load)
            # 将第一行器件数据导入模板1中
            sheet1 = wb.sheets['%s' % sheetnum]
            sheet1.range(cell_num[a] + '2').options(transpose=True).value = ig_list
            sheet1.range(cell_num[a + 1] + '2').options(transpose=True).value = id_list
        wb.save()
        wb.close()
        # 操作第二行器件数据
        wb = app.books.open(os.curdir + '\\数据处理\\后3-纵向对比2.xlsx')
        for each in file_flag2:
            os.chdir(os.curdir + '\\原始数据\\%dK' % i)
            sheetnum = each.split('.', 1)[1]
            # usecols 参数4、5分别为B1500输出csv文件中IG、ID所在列
            csv_data1 = pd.read_csv(os.curdir + '\\%s.csv' % each, usecols=[3], header=215, nrows=251, error_bad_lines=False)
            list1 = csv_data1.values.tolist()
            ig_list = []
            for each_ig in list1:
                ig_list.append(each_ig[0])
            csv_data2 = pd.read_csv(os.curdir + '\\%s.csv' % each, usecols=[4], header=215, nrows=251, error_bad_lines=False)
            list2 = csv_data2.values.tolist()
            id_list = []
            for each_id in list2:
                id_list.append(each_id[0])
            os.chdir(file_load)
            # 将第二行器件数据导入模板1中
            sheet1 = wb.sheets['%s' % sheetnum]
            sheet1.range(cell_num[a] + '2').options(transpose=True).value = ig_list
            sheet1.range(cell_num[a + 1] + '2').options(transpose=True).value = id_list
        wb.save()
        wb.close()
        # 操作第三行器件数据
        wb = app.books.open(os.curdir + '\\数据处理\\后3-纵向对比3.xlsx')
        for each in file_flag3:
            os.chdir(os.curdir + '\\原始数据\\%dK' % i)
            sheetnum = each.split('.', 1)[1]
            # usecols 参数4、5分别为B1500输出csv文件中IG、ID所在列
            csv_data1 = pd.read_csv(os.curdir + '\\%s.csv' % each, usecols=[3], header=215, nrows=251, error_bad_lines=False)
            list1 = csv_data1.values.tolist()
            ig_list = []
            for each_ig in list1:
                ig_list.append(each_ig[0])
            csv_data2 = pd.read_csv(os.curdir + '\\%s.csv' % each, usecols=[4], header=215, nrows=251, error_bad_lines=False)
            list2 = csv_data2.values.tolist()
            id_list = []
            for each_id in list2:
                id_list.append(each_id[0])
            os.chdir(file_load)
            # 将第三行器件数据导入模板1中
            sheet1 = wb.sheets['%s' % sheetnum]
            sheet1.range(cell_num[a] + '2').options(transpose=True).value = ig_list
            sheet1.range(cell_num[a + 1] + '2').options(transpose=True).value = id_list
        wb.save()
        wb.close()
        a += 2
        print('%dk数据已经全部提取并插入到后3-纵向对比模板中！！！' % i)


if __name__ == '__main__':
    topfile = input('请给出顶层文件夹路径：')
    lgtCont(topfile)
