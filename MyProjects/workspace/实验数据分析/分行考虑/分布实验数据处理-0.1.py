# coding: utf-8 #
#  author:李斌  #

# 导入模块
import pandas as pd
import os
import shutil
import xlwings as xw
import sys


def paraSum(file_load):
    """
    此程序功能为：将模板中提取的参数汇总到一个文件中，并进行必要的处理（删除异常数据）
    """
    os.mkdir(file_load + '\\数据处理\\分行处理')
    os.chdir(file_load + '\\数据处理\\分行处理')
    cycle_num = [3, 6, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    app = xw.App(visible=True, add_book=True)
    app.display_alerts = True
    app.screen_updating = True
    # 打开《参数汇总处理》文件
    shutil.copy(file_load + '\\其它模板\\参数汇总处理.xlsx', os.curdir)
    wb = app.books.open('参数汇总处理.xlsx')
    # 循环将数据提取出来并插入进 参数汇总处理.xlsx 的适当位置
    d = 1
    e = 1
    for i in cycle_num:
        excel_data1 = pd.read_excel(os.pardir + '\\参数提取\\%dK\\%dK-1.xlsx' % (i, i), sheet_name='参数提取',
                                    usecols=[a for a in [0, 1, 2, 3, 4, 5, 10, 11, 12]], header=0, error_bad_lines=False)
        excel_data2 = pd.read_excel(os.pardir + '\\参数提取\\%dK\\%dK-2.xlsx' % (i, i), sheet_name='参数提取',
                                    usecols=[a for a in [0, 1, 2, 3, 4, 5, 10, 11, 12]], header=0, error_bad_lines=False)
        list_df1 = excel_data1.values.tolist()
        list_df2 = excel_data2.values.tolist()
        list_df_transp = [['%dK相对' % i], ['%dK绝对' % i], ['%dK相对' % i], ['%dK绝对' % i], ['%dK相对' % i], ['%dK绝对' % i], ['%dK相对' % i], ['%dK绝对' % i], ['%dK' % i]]
        for a in range(0, 9):
            for b in range(0, 28):
                list_df_transp[a].append(list_df1[b][a])
        for a in range(0, 9):
            for b in range(0, 28):
                list_df_transp[a].append(list_df2[b][a])
        dev_flag = ['标号', '1_1', '1_2', '1_3', '1_4', '1_5', '1_6', '1_7', '1_8', '1_9', '1_10', '1_11', '1_12',
                    '1_13', '1_14', '1_15', '1_16', '1_17', '1_18', '1_19', '1_20', '1_21', '1_22', '1_23', '1_24',
                    '1_25', '1_26', '1_27', '1_28', '2_1', '2_2', '2_3', '2_4', '2_5', '2_6', '2_7', '2_8', '2_9',
                    '2_10', '2_11', '2_12', '2_13', '2_14', '2_15', '2_16', '2_17', '2_18', '2_19', '2_20', '2_21',
                    '2_22', '2_23', '2_24', '2_25', '2_26', '2_27', '2_28']
        colum_flag = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                      'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        c = 0
        for sht_num in range(0, 4):
            sheet = wb.sheets[sht_num]
            sheet.range('%s1' % colum_flag[0]).options(transpose=True).value = dev_flag
            sheet.range('%s1' % colum_flag[d]).options(transpose=True).value = list_df_transp[c]
            sheet.range('%s1' % colum_flag[d + 1]).options(transpose=True).value = list_df_transp[c+1]
            c += 2
        sheet2 = wb.sheets[4]
        sheet2.range('%s1' % colum_flag[0]).options(transpose=True).value = dev_flag
        sheet2.range('%s1' % colum_flag[e]).options(transpose=True).value = list_df_transp[c]
        e += 1
        d += 2
    print('数据已经全部转移到 参数汇总处理.xlsx 中！！！')
    wb.save()
    wb.close()
    # ----------------------------------------------------------------------------------------------------------------
    # 对 参数汇总处理.xlsx 中原始参数进行处理
    # 去负\正及异常
    a = 1
    b = 2
    c = 0
    d = 1
    wb = app.books.open('参数汇总处理.xlsx')
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
            else:
                error_list.append(int(each_error.split('.', 1)[1]) + 28)
        error_list.sort(reverse=True)
        # 已经得到 error_list
        # 处理 ion
        ion_df = pd.read_excel('参数汇总处理.xlsx', sheet_name='ion', usecols=[a], header=0)  # 取 ion 的相对变化值
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
        sheet_ionz = wb.sheets['ion(+)']
        sheet_ionf = wb.sheets['ion(-)']
        sheet_ionz.range('%s1' % colum_flag[c]).options(transpose=True).value = ion_list1
        sheet_ionf.range('%s1' % colum_flag[c]).options(transpose=True).value = ion_list2
        # 处理 vth截
        vthj_df = pd.read_excel('参数汇总处理.xlsx', sheet_name='vth截', usecols=[b], header=0)  # 取 vth截 的绝对变化值
        vthj_data = vthj_df.values.tolist()
        for each_error_num in error_list:  # 去异常项
            del vthj_data[each_error_num - 1]
        vthj_list1 = ['%dK' % i]
        vthj_list2 = ['%dK' % i]
        for each_vthj in vthj_data:
            if each_vthj[0] >= 0:  # 去负项
                vthj_list1.append(each_vthj[0])
            else:  # 去正项
                vthj_list2.append(each_vthj[0])
        sheet_vthjz = wb.sheets['vth截(+)']
        sheet_vthjf = wb.sheets['vth截(-)']
        sheet_vthjz.range('%s1' % colum_flag[c]).options(transpose=True).value = vthj_list1
        sheet_vthjf.range('%s1' % colum_flag[c]).options(transpose=True).value = vthj_list2
        # 处理 vth定
        vthd_df = pd.read_excel('参数汇总处理.xlsx', sheet_name='vth定', usecols=[b], header=0)  # 取 vth定 的绝对变化值
        vthd_data = vthd_df.values.tolist()
        for each_error_num in error_list:  # 去异常项
            del vthd_data[each_error_num - 1]
        vthd_list1 = ['%dK' % i]
        vthd_list2 = ['%dK' % i]
        for each_vthd in vthd_data:
            if each_vthd[0] >= 0:  # 去负项
                vthd_list1.append(each_vthd[0])
            else:  # 去正项
                vthd_list2.append(each_vthd[0])
        sheet_vthdz = wb.sheets['vth定(+)']
        sheet_vthdf = wb.sheets['vth定(-)']
        sheet_vthdz.range('%s1' % colum_flag[c]).options(transpose=True).value = vthd_list1
        sheet_vthdf.range('%s1' % colum_flag[c]).options(transpose=True).value = vthd_list2
        # 处理Ioff 相对变化值
        ion_df = pd.read_excel('参数汇总处理.xlsx', sheet_name='ioff', usecols=[a], header=0)  # 取 ioff 的相对变化值
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
        sheet_ionz = wb.sheets['ioff相(+)']
        sheet_ionf = wb.sheets['ioff相(-)']
        sheet_ionz.range('%s1' % colum_flag[c]).options(transpose=True).value = ion_list1
        sheet_ionf.range('%s1' % colum_flag[c]).options(transpose=True).value = ion_list2
        # 处理Ioff 绝对变化值
        ion_df = pd.read_excel('参数汇总处理.xlsx', sheet_name='ioff', usecols=[b], header=0)  # 取 ioff 的绝对变化值
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
        sheet_ionz = wb.sheets['ioff绝(+)']
        sheet_ionf = wb.sheets['ioff绝(-)']
        sheet_ionz.range('%s1' % colum_flag[c]).options(transpose=True).value = ion_list1
        sheet_ionf.range('%s1' % colum_flag[c]).options(transpose=True).value = ion_list2
        # 处理Ioff的值
        ion_df = pd.read_excel('参数汇总处理.xlsx', sheet_name='ioff值', usecols=[d], header=0)  # 取 ioff 的值
        ion_data = ion_df.values.tolist()
        for each_error_num in error_list:  # 去异常项
            del ion_data[each_error_num - 1]
        ion_list = ['%dK' % i]
        for each_ion in ion_data:
            ion_list.append(each_ion[0])
        sheet_ionz = wb.sheets['ioff值']
        sheet_ionz.range('%s1' % colum_flag[c]).options(transpose=True).value = ion_list
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
    print('汇总参数处理完毕！！！')
    wb.save()
    wb.close()
    app.quit()
    os.chdir(file_load)


def cumPer(file_load):
    """
    此函数的功能为：读取/写入数据并处理，得到累积百分比图数据格式
    """
    cycle_num = [3, 6, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    colum_flag = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                  'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    os.chdir(file_load + '\\数据处理\\分行处理')
    app = xw.App(visible=True, add_book=True)
    app.display_alerts = True
    app.screen_updating = True
    shutil.copy(file_load + '\\其它模板\\累积百分比图.xlsx', os.curdir)
    wb = app.books.open('累积百分比图.xlsx')
    a = 0
    b = 0
    for i in cycle_num:
        # 处理ion数据
        excel_data = pd.read_excel(os.curdir + '\\参数汇总处理.xlsx', sheet_name='ion(+)', usecols=[a], header=0,
                                   error_bad_lines=False)
        excel_data.dropna(inplace=True)
        list_df = excel_data.values.tolist()
        data_num = len(list_df)
        data_max = max(list_df)
        data_list = []
        for every_df in range(0, data_num):
            data_list.append(list_df[every_df][0]/data_max[0])
        data_list.sort()
        data_list.insert(0, '%dK' % i)
        sheet = wb.sheets['ion 去负及异常']
        sheet.range('%s1' % colum_flag[b]).options(transpose=True).value = data_list
        per_list = []
        for every_df in range(1, data_num + 1):
            per_list.append(every_df/data_num)
        per_list.insert(0, '%dK百分比' % i)
        sheet.range('%s1' % colum_flag[b + 1]).options(transpose=True).value = per_list
        # 处理vth截数据
        excel_data = pd.read_excel(os.curdir + '\\参数汇总处理.xlsx', sheet_name='vth截(+)', usecols=[a], header=0,
                                   error_bad_lines=False)
        excel_data.dropna(inplace=True)
        list_df = excel_data.values.tolist()
        data_num = len(list_df)
        data_max = max(list_df)
        data_list = []
        for every_df in range(0, data_num):
            data_list.append(list_df[every_df][0]/data_max[0])
        data_list.sort()
        data_list.insert(0, '%dK' % i)
        sheet = wb.sheets['vth截 去负及异常']
        sheet.range('%s1' % colum_flag[b]).options(transpose=True).value = data_list
        per_list = []
        for every_df in range(1, data_num + 1):
            per_list.append(every_df/data_num)
        per_list.insert(0, '%dK百分比' % i)
        sheet.range('%s1' % colum_flag[b + 1]).options(transpose=True).value = per_list
        # 处理vth定数据
        excel_data = pd.read_excel(os.curdir + '\\参数汇总处理.xlsx', sheet_name='vth定(+)', usecols=[a], header=0,
                                   error_bad_lines=False)
        excel_data.dropna(inplace=True)
        list_df = excel_data.values.tolist()
        data_num = len(list_df)
        data_max = max(list_df)
        data_list = []
        for every_df in range(0, data_num):
            data_list.append(list_df[every_df][0]/data_max[0])
        data_list.sort()
        data_list.insert(0, '%dK' % i)
        sheet = wb.sheets['vth定 去负及异常']
        sheet.range('%s1' % colum_flag[b]).options(transpose=True).value = data_list
        per_list = []
        for every_df in range(1, data_num + 1):
            per_list.append(every_df/data_num)
        per_list.insert(0, '%dK百分比' % i)
        sheet.range('%s1' % colum_flag[b + 1]).options(transpose=True).value = per_list
        # 处理ioff相数据
        excel_data = pd.read_excel(os.curdir + '\\参数汇总处理.xlsx', sheet_name='ioff相(+)', usecols=[a], header=0,
                                   error_bad_lines=False)
        excel_data.dropna(inplace=True)
        list_df = excel_data.values.tolist()
        data_num = len(list_df)
        try:
            data_max = max(list_df)
        except ValueError:
            data_max = 1
        data_list = []
        for every_df in range(0, data_num):
            data_list.append(list_df[every_df][0]/data_max[0])
        data_list.sort()
        data_list.insert(0, '%dK' % i)
        sheet = wb.sheets['ioff相 去负及异常']
        sheet.range('%s1' % colum_flag[b]).options(transpose=True).value = data_list
        per_list = []
        for every_df in range(1, data_num + 1):
            per_list.append(every_df/data_num)
        per_list.insert(0, '%dK百分比' % i)
        sheet.range('%s1' % colum_flag[b + 1]).options(transpose=True).value = per_list
        # 处理ioff绝数据
        excel_data = pd.read_excel(os.curdir + '\\参数汇总处理.xlsx', sheet_name='ioff绝(+)', usecols=[a], header=0,
                                   error_bad_lines=False)
        excel_data.dropna(inplace=True)
        list_df = excel_data.values.tolist()
        data_num = len(list_df)
        try:
            data_max = max(list_df)
        except ValueError:
            data_max = 1
        data_list = []
        for every_df in range(0, data_num):
            data_list.append(list_df[every_df][0]/data_max[0])
        data_list.sort()
        data_list.insert(0, '%dK' % i)
        sheet = wb.sheets['ioff绝 去负及异常']
        sheet.range('%s1' % colum_flag[b]).options(transpose=True).value = data_list
        per_list = []
        for every_df in range(1, data_num + 1):
            per_list.append(every_df/data_num)
        per_list.insert(0, '%dK百分比' % i)
        sheet.range('%s1' % colum_flag[b + 1]).options(transpose=True).value = per_list
        a += 1
        b += 2
    wb.save()
    wb.close()
    app.quit()
    os.chdir(file_load)
    print('累积百分比图数据处理完毕！')


# def qqplot(file_load):
    """
    此函数功能为：
    """


def show_menu(file_load):
    prompt = '''
        ***** bingo.lee *****

       |--- 执行所有：A/a ---|
       |--- 参数汇总：S/s ---|
       |--- 累计百分：P/p ---|
       |--- 退出程序：Q/q ---|
       |--- 请输入指令代码：
    '''
    chosen = False
    choice = input(prompt)
    while not chosen:
        if choice not in 'AaSsPpQq':
            choice = input('指令输入错误，请重新输入：')
        else:
            chosen = True

    if choice == 'Q' or choice == 'q':
        sys.exit()
    if choice == 'A' or choice == 'a':
        try:
            shutil.rmtree(file_load + '\\数据处理\\分行处理')
        except FileNotFoundError:
            pass
        paraSum(file_load)
        cumPer(file_load)
        print('恭喜您，所有数据处理完毕！！！')
    if choice == 'S' or choice == 's':
        try:
            os.remove(file_load + '\\数据处理\\分行处理\\参数汇总处理.xlsx')
        except FileNotFoundError:
            pass
        paraSum(file_load)
        show_menu(file_load)
    if choice == 'P' or choice == 'p':
        try:
            os.remove(file_load + '\\数据处理\\分行处理\\累积百分比图.xlsx')
        except FileNotFoundError:
            pass
        cumPer(file_load)
        show_menu(file_load)


if __name__ == '__main__':
    topfile = input('请给出顶层文件夹路径：')
    show_menu(topfile)

# 113/ 1.4,1.12,1.20,1.21,1.28,2.10,2.11,2.12,2.17,2.18,2.20,2.24,2.28
# 112/ 1.3,1.19,2.8,2.20
