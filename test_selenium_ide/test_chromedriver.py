from selenium import webdriver
from time import sleep


def test_driver():
    url ="https://www.baidu.com"
    driver  = webdriver.Chrome()
    driver.get(url)
    # 测试成功，Chromedriver匹配成功
    sleep(2)
    driver.quit()


