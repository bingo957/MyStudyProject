"""
 有道翻译的破解 时间：2019/6/13 15/18
"""
# 导入模块，可以模拟浏览器的请求与相应
import requests
import time
import random
import hashlib
import json  # 是一种数据解析方法
# from urllib import parse # 建议其他两种
# import aiohttp # 异步/协程模块


# 正常爬虫流程
def make_md5(string):
    """将字符串进行 信息摘要算法 加密"""
    string = string.encode('utf-8')
    md5_string = hashlib.md5(string).hexdigest()  # 转化成摘要
    return md5_string


def translate_word(_word_):
    # 【0】 网址
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    ua = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
          '64.0.3282.140 Safari/''537.36 Edge/17.17134 ')
    # JS破解
    t = make_md5(ua)
    r = str(int(time.time() * 1000))
    i = r + str(random.randint(0, 9))
    e = _word_
    salt = i
    sign = make_md5("fanyideskweb" + e + i + "@6f#X3=cCuncYssPsuRUE")
    ts = r
    bv = t
    # 请求正文（数据）
    data = {'action': 'FY_BY_CLICKBUTTION',
            'bv': bv,
            'client': 'fanyideskweb',
            'doctype': 'json',
            'from': 'AUTO',
            'i': e,  # 需要翻译的对象
            'keyfrom': 'fanyi.web',
            'salt': salt,
            'sign': sign,
            'smartresult': 'dict',
            'to': 'AUTO',
            'ts': ts,
            'version': '2.1',
            }  # 数据是一个字典 要发送的数据
    headers = {'Accept': 'application/json, text/javascript, */*; q=0.01',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-Hans-CN, zh-Hans; q=0.5',
               'Cache-Control': 'no-cache',
               'Connection': 'Keep-Alive',
               'Content-Length': '246',
               'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'Cookie': ('OUTFOX_SEARCH_USER_ID=620234973@10.169.0.84; OUTFOX_SEARCH_USER_ID_NCOO=1891152210.750806;'
                          ' JSESSIONID=aaaUwTO7CHQG5gNIXKpTw; ___rl__test__cookies=1560408828769'),
               'Host': 'fanyi.youdao.com',
               'Origin': 'http://fanyi.youdao.com',
               'Referer': 'http://fanyi.youdao.com/',
               'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'),
               'X-Requested-With': 'XMLHttpRequest',
               }  # 请求头是一个字典
    # 发出请求 传出数据 得到响应
    response = requests.post(url, data=data, headers=headers)
    res_str = json.loads(response.text)  # json.loads 中的对象只能是 str
    #  res_str = response.json() 用这种方法不用 import json
    print('=============i love fishC.com=============')
    print(res_str['translateResult'][0][0]['tgt'])
    for i in res_str['smartResult']['entries']:
        print(i, end='')
    print('=============i love fishC.com=============', '\n')

# 函数程序调用
while True:
    word = input('请输入需要翻译的单词：')
    translate_word(word)
