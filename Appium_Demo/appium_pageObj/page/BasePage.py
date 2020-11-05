'''
 BasePage.py模块：作为基类，初始化封装driver
                 并且封装基本的方法
'''
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, locator):
        '''封装查找元素的操作'''
        return self.driver.find_element(by, locator)



    def find_and_click(self,by, locator):
        '''封装查找元素并点击的操作'''
        self.driver.find_element(by, locator).click()



    def find_by_scroll(self, text):
        '''封装滚动查找元素的操作'''
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        f'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("{text}").instance(0));')

    def get_toast_text(self):
        result = self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        return result
