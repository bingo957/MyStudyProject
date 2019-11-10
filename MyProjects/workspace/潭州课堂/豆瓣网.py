from selenium import webdriver
import time
from lxml import etree

# 1. 调用谷歌浏览器请求豆瓣网
driver = webdriver.Chrome()
driver.get("https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85%E7%89%87&type=11&interval_id=100:90&action=")
time.sleep(2)
html = driver.page_source
driver.close()

# 2. 抽取想要的数据
html = etree.HTML(html)  # 整理HTML文档对象
tit_list = html.xpath('//span[@class="movie-name-text"]/a/text()')
data_list = html.xpath('//div[@class="movie-misc"]/text()')
rate_list = html.xpath('//span[@class="rating_num"]/text()')
numb_list = html.xpath('//span[@class="comment-num"]/text()')
for tit, data, rate, numb in zip(tit_list, data_list, rate_list, numb_list):
    content = tit, data, rate, numb
    print(content)
    # 3. 数据保存
    with open("douban.txt", "a") as f:
        f.write(str(content) + "\n")
