from selenium.webdriver.common.by import By

from Appium_Demo.frame_demo.Pages.BasePage import BasePage
from Appium_Demo.frame_demo.Pages.SearchPage import SearchPage


class MarketPage(BasePage):

    def goto_search(self):
        self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']").click()
        return SearchPage()