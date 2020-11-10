from selenium.webdriver.common.by import By

from Appium_Demo.frame_demo.Pages.BasePage import BasePage
from Appium_Demo.frame_demo.Pages.SearchPage import SearchPage


class MarketPage(BasePage):

    def goto_search(self):
        path = '../yamls/market.yaml'
        func_name = 'goto_search'
        self.yaml_parse(path, func_name)
        # self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']").click()
        return SearchPage(self.driver)