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


def select_positive(file_load):
    """
    函数功能：
    """
    os.chdir(file_load + r'\数据处理')
    colum_flag = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                  'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    app = xw.App(visible=True, add_book=True)
    app.display_alerts = True
    app.screen_updating = True
    wb = app.books.add()
    wb.sheets.add('select_vth')
    wb.sheets.add('select_ion')
    wb.sheets.add('vth')
    wb.sheets.add('ion')
    # 取ion相对值
    sheet_ion = wb.sheets['ion']
    pd_excel1 = pd.read_excel('参数汇总处理.xlsx', sheet_name='ion', usecols=[0], header=None)
    flag_data = pd_excel1.values.tolist()
    flag_list = []
    for each_flag_data in flag_data:
        flag_list.append(each_flag_data[0])
    sheet_ion.range('A1').options(transpose=True).value = flag_list
    b = 1
    for a in range(1, 24, 2):
        pd_excel2 = pd.read_excel('参数汇总处理.xlsx', sheet_name='ion', usecols=[a], header=None)
        ion_data = pd_excel2.values.tolist()
        ion_list = []
        for each_ion_data in ion_data:
            ion_list.append(each_ion_data[0])
        sheet_ion.range('%s1' % colum_flag[b]).options(transpose=True).value = ion_list
        b += 1
    # 取vth相对值
    sheet_vth = wb.sheets['vth']
    b = 0
    for a in range(0, 25, 2):
        pd_excel3 = pd.read_excel('参数汇总处理.xlsx', sheet_name='ion', usecols=[a], header=None)
        vth_data = pd_excel3.values.tolist()
        vth_list = []
        for each_vth_data in vth_data:
            vth_list.append(each_vth_data[0])
        sheet_vth.range('%s1' % colum_flag[b]).options(transpose=True).value = vth_list
        b += 1
    wb.save('全正器件筛选.xlsx')
    wb.close()
    # 处理数据（选正器件/去异常器件）
    print('请注意下方输入时必须输入英文字符！！！')
    error_ifo = input('请输入异常器件标号（格式：1.12,2.10,3.12）：')  # 注意输入法必须是英文
    error_dev = []
    if error_ifo == '':
        pass
    else:
        for esch_error_dev in error_ifo.split(','):
            error_dev.append(esch_error_dev.replace('.', '_'))
    # 已经得到error_dev
    # 读取并去掉异常器件
    wb = app.books.open('全正器件筛选.xlsx')
    # ion处理
    pd_excel4 = pd.read_excel('全正器件筛选.xlsx', sheet_name='ion', header=None)
    sheet_select_ion = wb.sheets['select_ion']
    index1 = True
    index2 = True
    c = 1
    for row in range(0, pd_excel4.shape[0]):
        row_data = pd_excel4.iloc[row][0:30].tolist()
        if row_data[0] in error_dev:
            index1 = False
        for every_row_data in row_data:
            if isinstance(every_row_data, float):
                if every_row_data < 0:
                    index2 = False
        if index1 is True and index2 is True:
            sheet_select_ion.range('A%d' % c).options(transpose=False).value = row_data
            c += 1
        index1 = True
        index2 = True
    # vth处理
    pd_excel5 = pd.read_excel('全正器件筛选.xlsx', sheet_name='vth', header=None)
    sheet_select_vth = wb.sheets['select_vth']
    index3 = True
    index4 = True
    d = 1
    for row in range(0, pd_excel5.shape[0]):
        row_data = pd_excel5.iloc[row][0:30].tolist()
        if row_data[0] in error_dev:
            index3 = False
        for every_row_data in row_data:
            if isinstance(every_row_data, float):
                if every_row_data < 0:
                    index4 = False
        if index3 is True and index4 is True:
            sheet_select_vth.range('A%d' % d).options(transpose=False).value = row_data
            d += 1
        index3 = True
        index4 = True
    wb.save()
    wb.close()
    app.quit()


if __name__ == '__main__':
    topfile = input('请给出顶层文件夹路径：')
    select_positive(topfile)

# 113/ 1.4,1.12,1.20,1.21,1.28,2.10,2.11,2.12,2.17,2.18,2.20,2.24,2.28,3.3,3.6,3.8,3.15,3.21,3.22,3.23,3.24
# 112/ 1.2,1.3,1.4,1.12,1.19,1.20,2.8,2.20,3.2,3.12,3.13
