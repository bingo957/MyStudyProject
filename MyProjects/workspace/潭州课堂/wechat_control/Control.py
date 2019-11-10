#!/usr/bin/python3
# @Time      : 2019/5/25 13:07
# @Author    : 老杨
# @FileName  : Order.py
# @Software  : PyCharm
# pip install pypiwin32
# pip install pyttsx3
import os
import win32api
import pyttsx3


class Order:
    def set_order(self, orderName, path):
        """
        设置指令，判断指令
        :param orderName: 指令名称
        :param path: 程序路径
        :return: None
        """
        if orderName == ''or path == '':
            raise Exception('请补充完整您的指令名称或路径')
        try:
            file = self.get_order(orderName)
            if file is None:
                self.add_order(orderName, path)
                self.tell('指令添加成功')
            else:
                self.tell('当前指令已经存在')
        except FileNotFoundError:
            self.tell('我是你的贾维斯')
            self.add_order(orderName, path)

    def add_order(self, orderName, path):
        """
        添加指令
        :param orderName: 指令名称
        :param path: 程序路径
        :return: None
        """
        data = orderName + '路径为->' + path + '\n'
        with open('order.txt', 'a+', encoding='utf-8') as f:
            f.write(data)
        self.tell('指令添加成功')

    @staticmethod
    def get_order(name, returnData='orderPath'):
        """
        根据指令，获取对应值
        :param name: 指令名称
        :param returnData:返回的结果
        :return:返回指定结果
        """
        with open('order.txt', 'r+', encoding='utf-8') as f:
            data = f.readlines()
        for key, value in enumerate(data):
            result = value.split('路径为->')
            try:
                response = dict()
                response['orderName'] = result[0].replace('\n', '').strip()
                if name == response['orderName']:
                    response['orderPath'] = result[1].replace('\n', '').strip()
                    response['exeName'] = response['orderPath'][response['orderPath'].rfind('\\')+1:]
                    return response[returnData]
            except TypeError:
                info = '第'+str(key)+'行不符合格式\n请按格式修改'
                exit(info)
                # raise Exception(info)

    # https://www.cnblogs.com/xknight/articles/1291111.html
    def startOrder(self, orderName, hwnd=0, op='open', params='', dirs='', bShow=1):
        """
        根据指令，打开相应程序
        :param orderName: 指令名
        :param hwnd: 父窗口的句柄，如果没有父窗口，则为0。
        :param op: 要进行的操作，为“open”、“print”或者为空。
        :param params: 要运行的程序，或者打开的脚本。
        :param dirs: 要向程序传递的参数，如果打开的为文件，则为空。
        :param bShow: 是否显示窗口。
        :return: None
        """
        file = self.get_order(orderName)
        if file is None:
            self.tell('没有找到对应的指令')
        else:
            win32api.ShellExecute(hwnd, op, file, params, dirs, bShow)
            self.tell('正在打开'+orderName)

    @staticmethod
    def tell(data):
        """
        语音提醒
        :param data: 需要提醒的话
        :return:
        """
        engine = pyttsx3.init()
        engine.say(data)
        engine.runAndWait()

    def stopOrder(self, orderName):
        """
        关闭程序
        :param orderName: 指令名
        :return:
        """
        file = self.get_order(orderName)
        if file is None:
            res = 'TASKKILL /F /IM '+self.get_order(orderName, 'exeName')
            os.system(res)
            self.tell(orderName+'已经退出')
        else:
            self.tell('没有找到对应的指令')

    def run(self, orderName):
        """
        运行指令
        :param orderName: 需要执行的指令
        :return: None
        """
        if orderName == '关机':
            self.tell('即将为您关闭电脑')
            os.system('shutdown /s /t 0')
        elif orderName == '重启':
            self.tell('即将为您重启电脑')
            os.system('shutdown /r /t 0')
        else:
            keyWord = orderName[0:2]
            orderWord = orderName[2:]
            if keyWord == '打开':
                self.startOrder(orderWord)
            elif keyWord == '退出':
                self.stopOrder(orderWord)
            else:
                # noinspection PyBroadException
                try:
                    os.system(orderName)
                except Exception:
                    self.tell('请输入正确指令')

# demo 添加指令
# test = Order()
# orderName = "微信"
# path ="C:\Program Files (x86)\Tencent\WeChat\WeChat.exe"
# test.set_order(orderName,path)
