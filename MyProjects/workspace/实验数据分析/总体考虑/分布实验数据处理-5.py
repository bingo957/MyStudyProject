# coding: utf-8 #
#  author:李斌  #

# 导入模块
import pandas as pd
import os
import shutil
import xlwings as xw
import sys


def init2mould(file_load):
    """此程序功能为;将初始数据从csv文件中插入到模板文件中
       注意事项：
            1、三个模板文件夹和初始数据文件夹同在顶层文件之下！！！
            2、模板文件夹命名为：《0K模板》《0非K模板》，初始数据文件夹命名为《初始数据》！！！
            3、《0K模板》中模板文件命名为“0K-1.xlsx”“0K-2.xlsx”“0K-3.xlsx”！！！
            4、《0非K模板》中模板文件命名为“#K-1.xlsx”“#K-2.xlsx”“#K-3.xlsx”！！！
            5、《初始数据》中文件夹命名为“0K”“3K”“6K”等（K大写），当改变弯曲次数时，需要更改程序中cycle_num变量！！！
            6、初始数据表格命名格式为：“1.1”“1.2”“1.3”“2.1”“3.1”等！！！
    """
    # 设置循环参数
    cycle_num = [0, 3, 6, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    file_flag1 = ['1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '1.8', '1.9', '1.10', '1.11', '1.12', '1.13',
                  '1.14', '1.15', '1.16', '1.17', '1.18', '1.19', '1.20', '1.21', '1.22', '1.23', '1.24',
                  '1.25', '1.26', '1.27', '1.28']
    file_flag2 = ['2.1', '2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '2.9', '2.10', '2.11', '2.12', '2.13',
                  '2.14', '2.15', '2.16', '2.17', '2.18', '2.19', '2.20', '2.21', '2.22', '2.23', '2.24',
                  '2.25', '2.26', '2.27', '2.28']
    file_flag3 = ['3.1', '3.2', '3.3', '3.4', '3.5', '3.6', '3.7', '3.8', '3.9', '3.10', '3.11', '3.12', '3.13',
                  '3.14', '3.15', '3.16', '3.17', '3.18', '3.19', '3.20', '3.21', '3.22', '3.23', '3.24',
                  '3.25', '3.26', '3.27', '3.28']
    app = xw.App(visible=True, add_book=False)
    app.display_alerts = True
    app.screen_updating = True
    for i in cycle_num:
        os.chdir(file_load)
        if i == 0:
            # 首先从模板创建 0K 时的参数提取表格，这里模板文件夹位置必须与存放原始数据的文件夹同层！！！
            # 1、首先创建 0K 文件夹
            os.mkdir(os.curdir + '\\数据处理')
            os.mkdir(os.curdir + '\\数据处理\\参数提取')
            os.mkdir(os.curdir + '\\数据处理\\参数提取\\%dK' % i)
            # 2、将模板复制进 0K 文件夹并改名(0K不需要改名)，这里必须要有两个模板的文件夹！！！
            os.chdir(os.curdir + '\\数据处理\\参数提取\\%dK' % i)
            shutil.copy(file_load + '\\0K模板\\0K-1.xlsx', os.curdir)
            shutil.copy(file_load + '\\0K模板\\0K-2.xlsx', os.curdir)
            shutil.copy(file_load + '\\0K模板\\0K-3.xlsx', os.curdir)
            os.chdir(file_load)
            # 从 csv 文件中提取文件并插入到模板中
            # 操作第一行器件数据
            wb1 = app.books.open(os.curdir + '\\数据处理\\参数提取\\%dK\\0K-1.xlsx' % i)
            wb2 = app.books.open(os.curdir + '\\0非K模板\\#K-1.xlsx')
            for each in file_flag1:
                os.chdir(os.curdir + '\\原始数据\\%dK' % i)  # 此处注意必须创建’原始数据‘文件夹且内部文件格式为’0K‘！！！
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
                # 将第一行器件数据导入到0K模板1和#K模板1中
                sheet1 = wb1.sheets['%s' % sheetnum]
                sheet1.range('C2').options(transpose=True).value = ig_list
                sheet1.range('D2').options(transpose=True).value = id_list
                sheet2 = wb2.sheets['%s' % sheetnum]
                sheet2.range('C2').options(transpose=True).value = ig_list
                sheet2.range('D2').options(transpose=True).value = id_list
            wb1.save()
            wb2.save()
            wb1.close()
            wb2.close()
            # 操作第二行器件数据
            wb1 = app.books.open(os.curdir + '\\数据处理\\参数提取\\%dK\\0K-2.xlsx' % i)
            wb2 = app.books.open(os.curdir + '\\0非K模板\\#K-2.xlsx')
            for each in file_flag2:
                os.chdir(os.curdir + '\\原始数据\\%dK' % i)  # 此处注意必须创建’原始数据‘文件夹且内部文件格式为’0K‘！！！
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
                # 将第二行器件数据导入到0K模板1和#K模板1中
                sheet1 = wb1.sheets['%s' % sheetnum]
                sheet1.range('C2').options(transpose=True).value = ig_list
                sheet1.range('D2').options(transpose=True).value = id_list
                sheet2 = wb2.sheets['%s' % sheetnum]
                sheet2.range('C2').options(transpose=True).value = ig_list
                sheet2.range('D2').options(transpose=True).value = id_list
            wb1.save()
            wb2.save()
            wb1.close()
            wb2.close()
            # 操作第三行器件数据
            wb1 = app.books.open(os.curdir + '\\数据处理\\参数提取\\%dK\\0K-3.xlsx' % i)
            wb2 = app.books.open(os.curdir + '\\0非K模板\\#K-3.xlsx')
            for each in file_flag3:
                os.chdir(os.curdir + '\\原始数据\\%dK' % i)  # 此处注意必须创建’原始数据‘文件夹且内部文件格式为’0K‘！！！
                sheetnum = each.split('.', 1)[1]
                # usecols 参数4、5分别为B1500输出csv文件中IG、ID所在列
                csv_data1 = pd.read_csv(os.curdir + '\\%s.csv' % each, usecols=[3], header=215, nrows=251, error_bad_lines=False)
                list1 = csv_data1.values.tolist()
                ig_list = []
                for each_ig in list1:
                    ig_list.append(each_ig[0])
                csv_data2 = pd.read_csv(os.curdir + '\\%s.csv' % each, usecols=[4],  header=215, nrows=251, error_bad_lines=False)
                list2 = csv_data2.values.tolist()
                id_list = []
                for each_id in list2:
                    id_list.append(each_id[0])
                os.chdir(file_load)
                # 将第三行器件数据导入到0K模板1和#K模板1中
                sheet1 = wb1.sheets['%s' % sheetnum]
                sheet1.range('C2').options(transpose=True).value = ig_list
                sheet1.range('D2').options(transpose=True).value = id_list
                sheet2 = wb2.sheets['%s' % sheetnum]
                sheet2.range('C2').options(transpose=True).value = ig_list
                sheet2.range('D2').options(transpose=True).value = id_list
            wb1.save()
            wb2.save()
            wb1.close()
            wb2.close()
            print('0k数据已经全部提取并插入到模板中！！！')
        else:
            # 首先从模板创建 #K 时的参数提取表格，这里模板文件夹位置必须与存放原始数据的文件夹同层！！！
            # 1、首先创建 #K 文件夹
            os.mkdir(os.curdir + '\\数据处理\\参数提取\\%dK' % i)
            # 2、将模板复制进 #K 文件夹并改名(0K不需要改名)，这里必须要有两个模板的文件夹！！！
            os.chdir(os.curdir + '\\数据处理\\参数提取\\%dK' % i)
            shutil.copy(file_load + '\\0非K模板\\#K-1.xlsx', os.curdir)
            shutil.copy(file_load + '\\0非K模板\\#K-2.xlsx', os.curdir)
            shutil.copy(file_load + '\\0非K模板\\#K-3.xlsx', os.curdir)
            os.rename('#K-1.xlsx', '%dK-1.xlsx' % i)
            os.rename('#K-2.xlsx', '%dK-2.xlsx' % i)
            os.rename('#K-3.xlsx', '%dK-3.xlsx' % i)
            os.chdir(file_load)
            # 从 csv 文件中提取文件
            # 操作第一行器件数据
            wb = app.books.open(os.curdir + '\\数据处理\\参数提取\\%dK\\%dK-1.xlsx' % (i, i))
            for each in file_flag1:
                os.chdir(os.curdir + '\\原始数据\\%dK' % i)  # 此处注意必须创建’原始数据‘文件夹且内部文件格式为’0K‘！！！
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
                # 将第一行器件数据导入到#K模板中
                sheet = wb.sheets['%s' % sheetnum]
                sheet.range('K2').options(transpose=True).value = ig_list
                sheet.range('L2').options(transpose=True).value = id_list
            wb.save()
            wb.close()
            # 操作第二行器件数据
            wb = app.books.open(os.curdir + '\\数据处理\\参数提取\\%dK\\%dK-2.xlsx' % (i, i))
            for each in file_flag2:
                os.chdir(os.curdir + '\\原始数据\\%dK' % i)  # 此处注意必须创建’原始数据‘文件夹且内部文件格式为’0K‘！！！
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
                # 将第二行器件数据导入到#K模板中
                sheet = wb.sheets['%s' % sheetnum]
                sheet.range('K2').options(transpose=True).value = ig_list
                sheet.range('L2').options(transpose=True).value = id_list
            wb.save()
            wb.close()
            # 操作第三行器件数据
            wb = app.books.open(os.curdir + '\\数据处理\\参数提取\\%dK\\%dK-3.xlsx' % (i, i))
            for each in file_flag3:
                os.chdir(os.curdir + '\\原始数据\\%dK' % i)  # 此处注意必须创建’原始数据‘文件夹且内部文件格式为’0K‘！！！
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
                # 将第三行器件数据导入到#K模板中
                sheet = wb.sheets['%s' % sheetnum]
                sheet.range('K2').options(transpose=True).value = ig_list
                sheet.range('L2').options(transpose=True).value = id_list
            wb.save()
            wb.close()
            print('%dK数据已经全部提取并插入到模板中！！！' % i)
    app.quit()
    print('^v^所有数据已经全部提取并插入到模板中^v^')


def paraSum(file_load):
    """
    此程序功能为：将模板中提取的参数汇总到一个文件中，并进行必要的处理（删除异常数据）
    """
    os.chdir(file_load + '\\数据处理')
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
        excel_data1 = pd.read_excel(os.curdir + '\\参数提取\\%dK\\%dK-1.xlsx' % (i, i), sheet_name='参数提取',
                                    usecols=[a for a in [0, 1, 2, 3, 4, 5, 10, 11, 12]], header=0, error_bad_lines=False)
        excel_data2 = pd.read_excel(os.curdir + '\\参数提取\\%dK\\%dK-2.xlsx' % (i, i), sheet_name='参数提取',
                                    usecols=[a for a in [0, 1, 2, 3, 4, 5, 10, 11, 12]], header=0, error_bad_lines=False)
        excel_data3 = pd.read_excel(os.curdir + '\\参数提取\\%dK\\%dK-3.xlsx' % (i, i), sheet_name='参数提取',
                                    usecols=[a for a in [0, 1, 2, 3, 4, 5, 10, 11, 12]], header=0, error_bad_lines=False)
        list_df1 = excel_data1.values.tolist()
        list_df2 = excel_data2.values.tolist()
        list_df3 = excel_data3.values.tolist()
        list_df_transp = [['%dK相对' % i], ['%dK绝对' % i], ['%dK相对' % i], ['%dK绝对' % i], ['%dK相对' % i], ['%dK绝对' % i], ['%dK相对' % i], ['%dK绝对' % i], ['%dK' % i]]
        for a in range(0, 9):
            for b in range(0, 28):
                list_df_transp[a].append(list_df1[b][a])
        for a in range(0, 9):
            for b in range(0, 28):
                list_df_transp[a].append(list_df2[b][a])
        for a in range(0, 9):
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


def initUni(file_load):
    """
    此函数功能为：将0K参数复制进一个文件中，看器件初始特性的均一性。
    """
    os.chdir(file_load + '\\数据处理')
    app = xw.App(visible=True, add_book=True)
    app.display_alerts = True
    app.screen_updating = True
    # 复制《初始特性》文件，同时打开
    shutil.copy(file_load + '\\其它模板\\初始特性.xlsx', os.curdir)
    wb = app.books.open('初始特性.xlsx')
    # 循环将数据提取出来并插入进 初始特性.xls 的适当位置
    excel_data1 = pd.read_excel(os.curdir + '\\参数提取\\0K\\0K-1.xlsx', sheet_name='参数提取',
                                usecols=[a for a in range(0, 6)], header=0, error_bad_lines=False)
    excel_data2 = pd.read_excel(os.curdir + '\\参数提取\\0K\\0K-2.xlsx', sheet_name='参数提取',
                                usecols=[a for a in range(0, 6)], header=0, error_bad_lines=False)
    excel_data3 = pd.read_excel(os.curdir + '\\参数提取\\0K\\0K-3.xlsx', sheet_name='参数提取',
                                usecols=[a for a in range(0, 6)], header=0, error_bad_lines=False)
    list_df1 = excel_data1.values.tolist()
    list_df2 = excel_data2.values.tolist()
    list_df3 = excel_data3.values.tolist()
    list_df_transp = [['ion'], ['vth截'], ['vth定'], ['SS'], ['μ'], ['ioff']]
    for a in range(0, 6):
        for b in range(0, 28):
            list_df_transp[a].append(list_df1[b][a])
    for a in range(0, 6):
        for b in range(0, 28):
            list_df_transp[a].append(list_df2[b][a])
    for a in range(0, 6):
        for b in range(0, 28):
            list_df_transp[a].append(list_df3[b][a])
    for sht_num in range(0, 6):
        sheet = wb.sheets[sht_num]
        sheet.range('A1').options(transpose=True).value = list_df_transp[sht_num]
    print('数据已经全部转移到 初始特性.xlsx 中！！！')
    wb.save()
    wb.close()
    # 去异常
    wb = app.books.open('初始特性.xlsx')
    item = ['ion', 'vth截', 'vth定', 'SS', 'μ', 'ioff']
    print('请注意下方输入时必须输入英文字符！！！')
    error_ifo = input('请输入初始异常器件标号（格式：1.12,2.10,3.12）：')  # 注意输入法必须是英文
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
    # 已经得到 error_list
    for i in item:
        item_df = pd.read_excel('初始特性.xlsx', sheet_name='%s' % i, usecols=[0], header=0, skip_blank_lines=False)
        item_data = item_df.values.tolist()
        for each_error_num in error_list:  # 去异常项
            del item_data[each_error_num - 1]
        item_list = ['%s去异常' % i]
        for each_item_data in item_data:
            item_list.append(each_item_data[0])
        sheet_item = wb.sheets['%s' % i]
        sheet_item.range('B1').options(transpose=True).value = item_list
    wb.save()
    wb.close()
    app.quit()
    os.chdir(file_load)


def weibullPara(file_load):
    """
    此函数功能为：将去负/异常处理后的数据复制进weibull参数估计模板中
    """
    cycle_num = [3, 6, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    # 复制模板到数据处理文件夹
    os.chdir(file_load + '\\数据处理')
    shutil.copy(file_load + '\\其它模板\\威布尔参数估计（最大相关系数优化法）模板.xlsx', os.curdir)
    # 打开模板文件
    app = xw.App(visible=True, add_book=False)
    app.display_alerts = True
    app.screen_updating = True
    wb = app.books.open('威布尔参数估计（最大相关系数优化法）模板.xlsx')
    # 读取处理后的参数数据并排序
    a = 0
    for i in cycle_num:
        excel_data = pd.read_excel(os.curdir + '\\参数汇总处理.xlsx', sheet_name='ion(+)', usecols=[a], header=0,
                                   error_bad_lines=False).values.tolist()
        data_list = []
        for each_data in excel_data:
            data_list.append(each_data[0])
        # 将数据复制进参数估计模板
        sheet = wb.sheets['%dK' % i]
        data_list.sort()
        sheet.range('B2').options(transpose=True).value = data_list
        a += 1
    wb.save()
    wb.close()
    app.quit()
    os.chdir(file_load)
    print('威布尔参数估计完毕！！！')


def lgtCont(file_load):
    """
    此函数功能为：将初始数据插入到纵向对比模板中
    """
    # 设置循环参数
    cycle_num = [0, 3, 6, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    file_flag1 = ['1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '1.8', '1.9', '1.10', '1.11', '1.12', '1.13',
                  '1.14', '1.15', '1.16', '1.17', '1.18', '1.19', '1.20', '1.21', '1.22', '1.23', '1.24',
                  '1.25', '1.26', '1.27', '1.28']
    file_flag2 = ['2.1', '2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '2.9', '2.10', '2.11', '2.12', '2.13',
                  '2.14', '2.15', '2.16', '2.17', '2.18', '2.19', '2.20', '2.21', '2.22', '2.23', '2.24',
                  '2.25', '2.26', '2.27', '2.28']
    file_flag3 = ['3.1', '3.2', '3.3', '3.4', '3.5', '3.6', '3.7', '3.8', '3.9', '3.10', '3.11', '3.12', '3.13',
                  '3.14', '3.15', '3.16', '3.17', '3.18', '3.19', '3.20', '3.21', '3.22', '3.23', '3.24',
                  '3.25', '3.26', '3.27', '3.28']
    cell_num = ['C', 'D', 'G', 'H', 'K', 'L', 'O', 'P', 'S', 'T', 'W', 'X', 'AA', 'AB', 'AE', 'AF', 'AI', 'AJ', 'AM',
                'AN', 'AQ', 'AR', 'AU', 'AV', 'AY', 'AZ']
    app = xw.App(visible=True, add_book=False)
    app.display_alerts = False
    app.screen_updating = True
    # 将模板复制进《数据处理》文件夹
    os.chdir(file_load + '\\数据处理')
    shutil.copy(file_load + '\\其它模板\\纵向对比1.xlsx', os.curdir)
    shutil.copy(file_load + '\\其它模板\\纵向对比2.xlsx', os.curdir)
    shutil.copy(file_load + '\\其它模板\\纵向对比3.xlsx', os.curdir)
    os.chdir(file_load)
    a = 0
    for i in cycle_num:
        # 从 csv 文件中提取文件并插入到模板中
        # 操作第一行器件数据
        wb = app.books.open(os.curdir + '\\数据处理\\纵向对比1.xlsx')
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
        wb = app.books.open(os.curdir + '\\数据处理\\纵向对比2.xlsx')
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
        wb = app.books.open(os.curdir + '\\数据处理\\纵向对比3.xlsx')
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
        print('%dk数据已经全部提取并插入到纵向对比模板中！！！' % i)


def cumPer(file_load):
    """
    此函数的功能为：读取/写入数据并处理，得到累积百分比图数据格式
    """
    cycle_num = [3, 6, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    colum_flag = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                  'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    # 新建一个累积百分比图文件
    os.chdir(file_load + '\\数据处理')
    app = xw.App(visible=True, add_book=True)
    app.display_alerts = True
    app.screen_updating = True
    # 复制《初始特性》文件，同时打开
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
       |--- 参数提取：E/e ---|
       |--- 参数汇总：S/s ---|
       |--- 器件均一：O/o ---|
       |--- 威布参数：W/w ---|
       |--- 纵向对比：Z/z ---|
       |--- 累计百分：P/p ---|
       |--- 退出程序：Q/q ---|
       |--- 请输入指令代码：
    '''
    chosen = False
    choice = input(prompt)
    while not chosen:
        if choice not in 'AaSsOowWZzPpEeQq':
            choice = input('指令输入错误，请重新输入：')
        else:
            chosen = True

    if choice == 'Q' or choice == 'q':
        sys.exit()
    if choice == 'A' or choice == 'a':
        try:
            shutil.rmtree(file_load + '\\数据处理')
        except FileNotFoundError:
            pass
        init2mould(file_load)
        paraSum(file_load)
        initUni(file_load)
        weibullPara(file_load)
        lgtCont(file_load)
        cumPer(file_load)
        print('恭喜您，所有数据处理完毕！！！')
    if choice == 'E' or choice == 'e':
        try:
            shutil.rmtree(file_load + '\\数据处理\\参数提取')
        except FileNotFoundError:
            pass
        init2mould(file_load)
        show_menu(file_load)
    if choice == 'S' or choice == 's':
        try:
            os.remove(file_load + '\\数据处理\\参数汇总处理.xlsx')
        except FileNotFoundError:
            pass
        paraSum(file_load)
        show_menu(file_load)
    if choice == 'O' or choice == 'o':
        try:
            os.remove(file_load + '\\数据处理\\初始特性.xlsx')
        except FileNotFoundError:
            pass
        initUni(file_load)
        show_menu(file_load)
    if choice == 'W' or choice == 'w':
        try:
            os.remove(file_load + '\\数据处理\\威布尔参数估计（最大相关系数优化法）模板.xlsx')
        except FileNotFoundError:
            pass
        weibullPara(file_load)
        show_menu(file_load)
    if choice == 'Z' or choice == 'z':
        try:
            os.remove(file_load + '\\数据处理\\纵向对比1.xlsx')
            os.remove(file_load + '\\数据处理\\纵向对比2.xlsx')
            os.remove(file_load + '\\数据处理\\纵向对比3.xlsx')
        except FileNotFoundError:
            pass
        lgtCont(file_load)
        show_menu(file_load)
    if choice == 'P' or choice == 'p':
        try:
            os.remove(file_load + '\\数据处理\\累积百分比图.xlsx')
        except FileNotFoundError:
            pass
        cumPer(file_load)
        show_menu(file_load)


if __name__ == '__main__':
    topfile = input('请给出顶层文件夹路径：')
    show_menu(topfile)

# 113/ 1.4,1.12,1.20,1.21,1.28,2.10,2.11,2.12,2.17,2.18,2.20,2.24,2.28,3.3,3.6,3.8,3.15,3.21,3.22,3.23,3.24
# 112/ 1.3,1.19,2.8,2.20,3.2,3.13
