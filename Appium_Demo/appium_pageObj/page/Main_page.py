
'''
位于企业微信主页，跳转至通讯录
'''
from appium.webdriver.common.mobileby import MobileBy
from Appium_Demo.appium_pageObj.page.AddressList_page import AdressListPage
from Appium_Demo.appium_pageObj.page.BasePage import BasePage


class MainPage(BasePage):
    address_element = (MobileBy.XPATH, "//*[@text='通讯录']")


    def goto_message(self):
        pass

    def goto_Adresslist(self):
        '''
        进入到通讯录页
        '''
        self.find_and_click(*self.address_element)
        # self.driver.find_element(MobileBy.XPATH,'//*[@resource-id="com.tencent.wework:id/dqn" and @text="通讯录"]').click()
        return AdressListPage(self.driver)

    def goto_workshop(self):
        pass

    def got_mine(self):
        pass
