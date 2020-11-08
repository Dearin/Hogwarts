from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from Appium_Demo.frame_demo.Handles.handle_black import handle_black


class BasePage:
    '''
      做一些app的初始化
    '''
    # 设置一个黑名单,_var 是保护属性，无法在类外调用这个方法
    black_list = [(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")]
    max_num = 3
    error_num = 0

    def __init__(self, driver: WebDriver = None):

        if driver is None:
            desire_caps = {}
            desire_caps["platformName"] = "android"
            desire_caps["deviceName"] = "emulator-5554"
            desire_caps["appPackage"] = "com.xueqiu.android"
            desire_caps["appActivity"] = ".view.WelcomeActivityAlias"
            desire_caps["noReset"] = "true"  # 这里就避免来每次打开弹出的同意窗口
            desire_caps["skipDeviceInitialization"] = 'true'
            desire_caps["skipDriverInstallation"] = 'true'
            desire_caps["unicodeKeyBoard"] = "true"  # 输入中文字符
            desire_caps["browser"] = "Browser"  # 输入中文字符
            # 初始化驱动
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_caps)
            # 设置一个隐形等待，增加代码的健壮性
            self.driver.implicitly_wait(10)
        else:
            self.driver = driver

    @handle_black
    def find(self, by, locator=None):
        '''查找元素'''
        if locator is None:
            result = self.driver.find_element(*by)
        else:
            result = self.driver.find_element(by, locator)
        # --- 应保留的核心代代码end ---
        return result

    #解析yaml
    def parse(self,):
        pass