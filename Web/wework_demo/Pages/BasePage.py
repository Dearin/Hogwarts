'''
完成添加联系人功能，使用显式等待隐式等待结合的方式，练习课上的知识点。
'''
import logging
import shelve

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    '''
    BasePage用于进行页面的初始化的操作
    还有基本操作的封装：
    寻找元素/点击元素等
    '''
    # logger的设置
    root_logger = logging.getLogger()
    print(f"root_logger.handlers:{logging.getLogger().handlers}")
    for h in root_logger.handlers[:]:
        root_logger.removeHandler(h)
    logging.basicConfig(level=logging.INFO)

    # 需要访问的url: #后续的模块调用的时候，可以修改
    base_url = ''


    def __init__(self, driver: WebDriver = None):
        if driver == None:
            # 第一次初始化
            options = Options()
            options.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=options)
            self.driver.implicitly_wait(5)
        else:
            # 进行页面跳转的操作
            self.driver = driver

        # base_url 打开某个页面
        if self.base_url != "":
            self.driver.get(self.base_url)

    def teardown_method(self):
        self.driver.quit()


    def find(self, by, locator):
        logging.info(by)
        logging.info(locator)
        return  self.driver.find_element(by,locator)


    def find_and_click(self, by, locator):
        logging.info('find_and_click')
        logging.info(by)
        logging.info(locator)
        return self.find(by, locator).click()

    # def wait_for_click(self, locator, timeout=10):
    #     element: WebElement = WebDriverWait(self.driver, timeout).until(
    #         expected_conditions.element_to_be_clickable(locator))
    #     return element

    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)

    def wait_for_click(self, locator, timeout=10):
        element: WebElement = WebDriverWait(self.driver, timeout).until(
            expected_conditions.element_to_be_clickable(locator))
        return element
