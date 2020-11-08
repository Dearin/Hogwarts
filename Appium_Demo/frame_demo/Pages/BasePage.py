from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver



class BasePage:
    '''
      做一些app的初始化
    '''
    # 设置一个黑名单,_var 是保护属性，无法在类外调用这个方法
    _black_list = [(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")]
    _max_num = 3
    _error_num = 0

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
            self.driver.implicitly_wait(5)
        else:
            self.driver = driver

    def find(self, by, locator=None):
        '''查找元素'''
        # 当locator为空，也就是传入的元素只有一个(by, locator)时,需要解释器去解包
        # 做一些异常的处理
        try:
            if locator is None:
                result = self.driver.find_element(*by)
            else:
                result = self.driver.find_element(by, locator)
            # 找到元素，则将累计查找失败的数量重置为0
            self._error_num = 0
            return result
        except Exception as e:
            # 设置一个最大的查找次数，避免一直查找
            if self._error_num > self._max_num:
                raise e
            self._error_num += 1
            # 如果找不到元素，则遍历黑名单中的元素进行点击
            for black_ele in self._black_list:
                # 对元素在页面中进行查找
                ele = self.driver.find_elements(*black_ele)
                # 如果能查找出来元素，则对元素进行操作;注意ele存放的是一个数组[()]，数组第一个为对应的元素
                if len(ele) > 0 :
                    ele[0].click()
                    # 关闭掉弹窗后，再次查找原先的元素
                    return self.find(by, locator)
            raise e
