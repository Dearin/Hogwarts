from selenium.webdriver.common.by import By
from Appium_Demo.frame_demo.Pages.BasePage import BasePage
from Appium_Demo.frame_demo.Pages.MarketPage import MarketPage


class MainPage(BasePage):

    def goto_market(self):
        # 这里我们来模拟一个黑名单：点击登陆的图标，就会产生弹窗，影响我们正常的流程
        self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']").click()
        # 点击"行情"按钮，跳转值行情页面
        self.find(By.XPATH, "//*[@resource-id='android:id/tabs']//*[@text='行情']").click()
        return MarketPage(self.driver)