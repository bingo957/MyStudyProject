# coding: utf-8 #
#  author:李斌  #

# 导入模块
import pandas as pd
import os
import shutil
import xlwings as xw


def data_transfer(file_load):
    """
    函数功能：将原始数据提取出来并插入到相应文件（按器件分）中
    注意事项：
    1、“原始数据”文件夹在顶层路径下，“0K”、“1K”、“2.5K”、“5K”.....等文件下保存在“原始数据”文件夹下；
    2、“模板”文件夹在顶层路径下，“模板.xlsx”文件在“模板文件夹中”；
    3、原始数据 .csv 文件命名格式为：“2-2-0.1V“ ”2-2-5V“；
    4、文件以及文件夹的命名中英文字母均 大写；(严格区分大小写)
    """
    # 设置循环参数
    cycle_num = [0]
    w_flag = [2, 2.5, 3, 3.5, 4, 6, 8, 10, 15, 20, 30, 40]
    l_flag = [2, 2.5, 3, 3.5, 4, 5, 10]
    cell_num = {0: 'B1', 1: 'C1', 2: 'D1', 3: 'E1', 4: 'F1', 5: 'G1', 6: 'H1', 7: 'I1', 8: 'J1', 9: 'K1'}
    # 打开表格程序
    app = xw.App(visible=True, add_book=False)
    app.display_alerts = True
    app.screen_updating = True
    os.mkdir(file_load + '\\数据提取')
    os.chdir(file_load + '\\数据提取')
    if cycle_num[0] == 0:
        # 新建器件表格文件
        for w in w_flag:
            for l in l_flag:
                shutil.copy(file_load + '\\模板\\模板.xlsx', os.curdir)
                os.rename('模板.xlsx', '%s-%s.xlsx' % (w, l))
    else:
        pass
    # 设置循环
    i = cycle_num[0]
    for w in w_flag:
        for l in l_flag:
            # 打开表格文件
            wb = app.books.open('%s-%s.xlsx' % (w, l))
            # 提取 .csv文件中的数据
            # 0.1V-id
            csv_data_1_id = pd.read_csv(os.pardir + '\\原始数据\\%sK\\w=%s\\%s-%s\\%s-%s-0.1V.CSV' % (i, w, w, l, w, l), usecols=[4], header=215, error_bad_lines=False)
            list1 = csv_data_1_id.values.tolist()
            id_list_1 = ['%dK' % i]
            for each in range(251):
                id_list_1.append(list1[each][0])

            # 0.1V-ig
            csv_data_1_ig = pd.read_csv(os.pardir + '\\原始数据\\%sK\\w=%s\\%s-%s\\%s-%s-0.1V.CSV' % (i, w, w, l, w, l), usecols=[3], header=215, error_bad_lines=False)
            list2 = csv_data_1_ig.values.tolist()
            ig_list_1 = ['%dK' % i]
            for each in range(251):
                ig_list_1.append(list2[each][0])

            # 5V-id
            csv_data_5_id = pd.read_csv(os.pardir + '\\原始数据\\%sK\\w=%s\\%s-%s\\%s-%s-5V.CSV' % (i, w, w, l, w, l), usecols=[4], header=215, error_bad_lines=False)
            list3 = csv_data_5_id.values.tolist()
            id_list_2 = ['%dK' % i]
            for each in range(251):
                id_list_2.append(list3[each][0])

            # 5V-ig
            csv_data_5_ig = pd.read_csv(os.pardir + '\\原始数据\\%sK\\w=%s\\%s-%s\\%s-%s-5V.CSV' % (i, w, w, l, w, l), usecols=[3], header=215, error_bad_lines=False)
            list4 = csv_data_5_ig.values.tolist()
            ig_list_2 = ['%dK' % i]
            for each in range(251):
                ig_list_2.append(list4[each][0])
            # 将数据复制进模板中
            sheet1 = wb.sheets['ID(-0.1V)']
            sheet2 = wb.sheets['ID(-5V)']
            sheet3 = wb.sheets['IG(-0.1V)']
            sheet4 = wb.sheets['IG(-5V)']
            sheet1.range('%s' % cell_num[cycle_num[0]]).options(transpose=True).value = id_list_1
            sheet2.range('%s' % cell_num[cycle_num[0]]).options(transpose=True).value = id_list_2
            sheet3.range('%s' % cell_num[cycle_num[0]]).options(transpose=True).value = ig_list_1
            sheet4.range('%s' % cell_num[cycle_num[0]]).options(transpose=True).value = ig_list_2
            # 保存文件，
            wb.save()
            wb.close()
    # 关闭软件
    app.quit()


if __name__ == '__main__':
    topfile = input('请给出顶层文件夹路径：')
    data_transfer(topfile)
