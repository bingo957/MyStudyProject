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
    wb.sheets.add('vth截')
    wb.sheets.add('ion')
    # 对 参数汇总处理.xlsx 中原始参数进行处理
    # 去负\正及异常
    a = 1
    b = 2
    c = 1
    d = 1
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
        # 处理 ion
        ion_df = pd.read_excel('参数汇总处理.xlsx', sheet_name='ion', usecols=[a], header=0)  # 取 ion 的相对变化值
        ion_data = ion_df.values.tolist()
        for each_error_num in error_list:  # 去异常项
            ion_data[each_error_num - 1][0] = 'xxxxxxxx'
        ion_list = ['%dK' % i]
        for each_ion in ion_data:
            if each_ion[0] == 'xxxxxxxx':
                ion_list.append(each_ion[0])
            elif each_ion[0] >= 0:
                ion_list.append(each_ion[0])
            else:
                ion_list.append('xxxxxxxx')
        sheet_ion = wb.sheets['ion']
        sheet_ion.range('%s1' % colum_flag[c]).options(transpose=True).value = ion_list
        # 处理 vth截
        vthj_df = pd.read_excel('参数汇总处理.xlsx', sheet_name='vth截', usecols=[b], header=0)  # 取 vth截 的绝对变化值
        vthj_data = vthj_df.values.tolist()
        for each_error_num in error_list:  # 去异常项
            vthj_data[each_error_num - 1][0] = 'xxxxxxxx'
        vthj_list = ['%dK' % i]
        for each_vthj in vthj_data:
            if each_vthj[0] == 'xxxxxxxx':
                vthj_list.append(each_vthj[0])
            elif each_vthj[0] >= 0:
                vthj_list.append(each_vthj[0])
            else:
                vthj_list.append('xxxxxxxx')
        sheet_vthj = wb.sheets['vth截']
        sheet_vthj.range('%s1' % colum_flag[c]).options(transpose=True).value = vthj_list
        a += 2
        b += 2
        c += 1
        d += 1
    # 添加器件号
    device_df = pd.read_excel('参数汇总处理.xlsx', sheet_name='ion', usecols=[0], header=0)
    device_data = device_df.values.tolist()
    device_num = ['标号']
    for every_device_data in device_data:
        device_num.append(every_device_data[0])
    sheet_ion = wb.sheets['ion']
    sheet_vthj = wb.sheets['vth截']
    sheet_ion.range('A1').options(transpose=True).value = device_num
    sheet_vthj.range('A1').options(transpose=True).value = device_num
    print('汇总参数处理完毕！！！')
    wb.save('恢复观察-参数汇总处理.xlsx')
    wb.close()
    app.quit()
    os.chdir(file_load)


if __name__ == '__main__':
    topfile = input('请给出顶层文件夹路径：')
    paraSum(topfile)

# 112/ 1.3,1.19,2.8,2.20,3.2,3.13
