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


def paraSum(file_load):
    """
    此程序功能为：将模板中提取的参数汇总到一个文件中，并进行必要的处理（删除异常数据）
    """
    os.chdir(file_load + '\\数据处理')
    cycle_num = [3, 6, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    app = xw.App(visible=True, add_book=True)
    app.display_alerts = True
    app.screen_updating = True
    wb = app.books.add()
    wb.sheets.add('u绝(-)')
    wb.sheets.add('u相(-)')
    wb.sheets.add('SS绝(-)')
    wb.sheets.add('SS相(-)')
    wb.sheets.add('u绝(+)')
    wb.sheets.add('u相(+)')
    wb.sheets.add('SS绝(+)')
    wb.sheets.add('SS相(+)')
    wb.sheets.add('u')
    wb.sheets.add('SS')
    # 循环将数据提取出来并插入进 参数汇总处理.xlsx 的适当位置
    d = 1
    for i in cycle_num:
        excel_data1 = pd.read_excel(os.curdir + '\\参数提取\\%dK\\%dK-1.xlsx' % (i, i), sheet_name='参数提取',
                                    usecols=[a for a in [6, 7, 8, 9]], header=0, error_bad_lines=False)
        excel_data2 = pd.read_excel(os.curdir + '\\参数提取\\%dK\\%dK-2.xlsx' % (i, i), sheet_name='参数提取',
                                    usecols=[a for a in [6, 7, 8, 9]], header=0, error_bad_lines=False)
        excel_data3 = pd.read_excel(os.curdir + '\\参数提取\\%dK\\%dK-3.xlsx' % (i, i), sheet_name='参数提取',
                                    usecols=[a for a in [6, 7, 8, 9]], header=0, error_bad_lines=False)
        list_df1 = excel_data1.values.tolist()
        list_df2 = excel_data2.values.tolist()
        list_df3 = excel_data3.values.tolist()
        list_df_transp = [['%dK相对' % i], ['%dK绝对' % i], ['%dK相对' % i], ['%dK绝对' % i]]
        for a in range(0, 4):
            for b in range(0, 28):
                list_df_transp[a].append(list_df1[b][a])
        for a in range(0, 4):
            for b in range(0, 28):
                list_df_transp[a].append(list_df2[b][a])
        for a in range(0, 4):
            for b in range(0, 28):
                list_df_transp[a].append(list_df3[b][a])
        dev_flag = ['标号', '1_1', '1_2', '1_3', '1_4', '1_5', '1_6', '1_7', '1_8', '1_9', '1_10', '1_11', '1_12',
                    '1_13', '1_14', '1_15', '1_16', '1_17', '1_18', '1_19', '1_20', '1_21', '1_22', '1_23', '1_24',
                    '1_25', '1_26', '1_27', '1_28', '2_1', '2_2', '2_3', '2_4', '2_5', '2_6', '2_7', '2_8', '2_9',
                    '2_10', '2_11', '2_12', '2_13', '2_14', '2_15', '2_16', '2_17', '2_18', '2_19', '2_20', '2_21',
                    '2_22', '2_23', '2_24', '2_25', '2_26', '2_27', '2_28', '3_1', '3_2', '3_3', '3_4', '3_5', '3_6',
                    '3_7', '3_8', '3_9', '3_10', '3_11', '3_12', '3_13', '3_14', '3_15', '3_16', '3_17', '3_18', '3_19',
                    '3_20', '3_21', '3_22', '3_23', '3_24', '3_25', '3_26', '3_27', '3_28']
        colum_flag = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                      'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        c = 0
        for sht_num in range(0, 2):
            sheet = wb.sheets[sht_num]
            sheet.range('%s1' % colum_flag[0]).options(transpose=True).value = dev_flag
            sheet.range('%s1' % colum_flag[d]).options(transpose=True).value = list_df_transp[c]
            sheet.range('%s1' % colum_flag[d + 1]).options(transpose=True).value = list_df_transp[c+1]
            c += 2
        d += 2
    print('数据已经全部转移到 其它参数汇总处理.xlsx 中！！！')
    wb.save('其它参数汇总处理.xlsx')
    wb.close()
    # ----------------------------------------------------------------------------------------------------------------
    # 对 其它参数汇总处理.xlsx 中原始参数进行处理
    # 去负\正及异常
    a = 1
    b = 2
    c = 0
    d = 1
    wb = app.books.open('其它参数汇总处理.xlsx')
    for i in cycle_num:
        print('请注意下方输入时必须输入英文字符！！！')
        error_ifo = input('请输入%dK异常器件标号（格式：1.12,2.10,3.12）：' % i)  # 注意输入法必须是英文
        if error_ifo == '':
            error_dev = []
        else:
            error_dev = error_ifo.split(',')
        colum_flag = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                      'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        error_list = []
        for each_error in error_dev:
            if each_error.split('.', 1)[0] == '1':
                error_list.append(int(each_error.split('.', 1)[1]))
            elif each_error.split('.', 1)[0] == '2':
                error_list.append(int(each_error.split('.', 1)[1]) + 28)
            else:
                error_list.append(int(each_error.split('.', 1)[1]) + 56)
        error_list.sort(reverse=True)
        # 已经得到 error_list
        # 处理 SS相
        ion_df = pd.read_excel('其它参数汇总处理.xlsx', sheet_name='SS', usecols=[a], header=0)  # 取 SS 的相对变化值
        ion_data = ion_df.values.tolist()
        for each_error_num in error_list:  # 去异常项
            del ion_data[each_error_num - 1]
        ion_list1 = ['%dK' % i]
        ion_list2 = ['%dK' % i]
        for each_ion in ion_data:
            if each_ion[0] >= 0:  # 去负项
                ion_list1.append(each_ion[0])
            else:  # 去正项
                ion_list2.append(each_ion[0])
        sheet_ionz = wb.sheets['SS相(+)']
        sheet_ionf = wb.sheets['SS相(-)']
        sheet_ionz.range('%s1' % colum_flag[c]).options(transpose=True).value = ion_list1
        sheet_ionf.range('%s1' % colum_flag[c]).options(transpose=True).value = ion_list2
        # 处理 SS绝
        ion_df = pd.read_excel('其它参数汇总处理.xlsx', sheet_name='SS', usecols=[a + 1], header=0)  # 取 SS 的相对变化值
        ion_data = ion_df.values.tolist()
        for each_error_num in error_list:  # 去异常项
            del ion_data[each_error_num - 1]
        ion_list1 = ['%dK' % i]
        ion_list2 = ['%dK' % i]
        for each_ion in ion_data:
            if each_ion[0] >= 0:  # 去负项
                ion_list1.append(each_ion[0])
            else:  # 去正项
                ion_list2.append(each_ion[0])
        sheet_ionz = wb.sheets['SS绝(+)']
        sheet_ionf = wb.sheets['SS绝(-)']
        sheet_ionz.range('%s1' % colum_flag[c]).options(transpose=True).value = ion_list1
        sheet_ionf.range('%s1' % colum_flag[c]).options(transpose=True).value = ion_list2
        # 处理 u相
        ion_df = pd.read_excel('其它参数汇总处理.xlsx', sheet_name='u', usecols=[a], header=0)  # 取 SS 的相对变化值
        ion_data = ion_df.values.tolist()
        for each_error_num in error_list:  # 去异常项
            del ion_data[each_error_num - 1]
        ion_list1 = ['%dK' % i]
        ion_list2 = ['%dK' % i]
        for each_ion in ion_data:
            if each_ion[0] >= 0:  # 去负项
                ion_list1.append(each_ion[0])
            else:  # 去正项
                ion_list2.append(each_ion[0])
        sheet_ionz = wb.sheets['u相(+)']
        sheet_ionf = wb.sheets['u相(-)']
        sheet_ionz.range('%s1' % colum_flag[c]).options(transpose=True).value = ion_list1
        sheet_ionf.range('%s1' % colum_flag[c]).options(transpose=True).value = ion_list2
        # 处理 u绝
        ion_df = pd.read_excel('其它参数汇总处理.xlsx', sheet_name='u', usecols=[a + 1], header=0)  # 取 SS 的相对变化值
        ion_data = ion_df.values.tolist()
        for each_error_num in error_list:  # 去异常项
            del ion_data[each_error_num - 1]
        ion_list1 = ['%dK' % i]
        ion_list2 = ['%dK' % i]
        for each_ion in ion_data:
            if each_ion[0] >= 0:  # 去负项
                ion_list1.append(each_ion[0])
            else:  # 去正项
                ion_list2.append(each_ion[0])
        sheet_ionz = wb.sheets['u绝(+)']
        sheet_ionf = wb.sheets['u绝(-)']
        sheet_ionz.range('%s1' % colum_flag[c]).options(transpose=True).value = ion_list1
        sheet_ionf.range('%s1' % colum_flag[c]).options(transpose=True).value = ion_list2
        # 在 Sheet1 中添加异常器件信息
        error_dev_ifo = []
        for error_dev_cout in range(len(error_dev)):
            error_dev_ifo.append(error_dev[error_dev_cout].replace('.', '_'))
        error_dev_ifo.insert(0, '%dK' % i)
        sheet_errorifo = wb.sheets['Sheet1']
        sheet_errorifo.range('%s1' % colum_flag[c]).options(transpose=True).value = error_dev_ifo
        a += 2
        b += 2
        c += 1
        d += 1
    print('汇总其它参数处理完毕！！！')
    wb.save()
    wb.close()
    app.quit()
    os.chdir(file_load)


if __name__ == '__main__':
    topfile = input('请给出顶层文件夹路径：')
    paraSum(topfile)

# 113/ 1.4,1.12,1.20,1.21,1.28,2.10,2.11,2.12,2.17,2.18,2.20,2.24,2.28,3.3,3.6,3.8,3.15,3.21,3.22,3.23,3.24
# 112/ 1.3,1.19,2.8,2.20,3.2,3.13
