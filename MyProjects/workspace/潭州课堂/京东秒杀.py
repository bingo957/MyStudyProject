from selenium import webdriver
import time
import datetime

# 1. 登录京东账户
driver = webdriver.Chrome()
driver.set_window_size(1280, 960)
driver.implicitly_wait(0.5)
print("start webdriver")
driver.get("https://passport.jd.com/uc/login?ltype=logout")
print("get web in")
while True:
    try:
        driver.find_element_by_link_text("jd_6577bf534...")
        print("已登录！")
        url = input("输入您需要抢购的商品链接：")
        driver.get(url)
        buy_time = "2019-06-15 21:42:00"
        print("buy_time:" + buy_time + "等待时间到达...")
        while True:
            now = datetime.datetime.now()
            print("当前北京时间：{}".format(now))
            # 3. 监控商品秒杀时间
            if now.strftime("%Y-%m-%d %H:%M:%S") == buy_time:
                # 4. 提交订单
                driver.find_element_by_id("btn-onkeybuy").click()
                driver.find_element_by_id("order-submit").click()
                print("-------已提交订单--------")
                break
        time.sleep(0.5)
    except:
        pass
