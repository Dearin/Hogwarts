'''
contactedit_page.py模块
主要进行成员信息的编辑/删除操作
'''
from appium.webdriver.common.mobileby import MobileBy

from Appium_Demo.appium_pageObj.page.BasePage import BasePage


class ContactEdit(BasePage):
    def contact_delete(self):
    # 找到对应删除按钮，点击删除
        print(self.driver.contexts)
        self.find_and_click(MobileBy.XPATH,'//*[@text="删除成员"]')
        print(self.driver.contexts)
    # 在弹窗中点击确认
        self.find_and_click(MobileBy.XPATH,'//*[@text="确定"]')
    # 人员删除成功后，会返回到通讯录页面
        from Appium_Demo.appium_pageObj.page.AddressList_page import AdressListPage
        return AdressListPage(self.driver)


    def contact_update(self):
        pass