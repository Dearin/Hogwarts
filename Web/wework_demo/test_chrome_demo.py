from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestChromeDemo:
    '''复用浏览器需要主要穿一个method参数'''
    def setup_method(self, method):
        options = Options()
        options.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(5)

    def teardown_method(self, method):
        self.driver.quit()

    def test_chrome_demo(self):
        self.driver.get("http://www.baidu.com")
        self.driver.implicitly_wait(5)

    def test_wework(self):
        '''当前已经打开了企业微信并扫码登陆了
        所有可以直接访问页面元素了
        '''
        self.driver.find_element(By.ID,"menu_contacts").click()
        sleep(3)
