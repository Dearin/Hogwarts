'''
个人信息页：
进行删除和其他编辑操作
'''
from appium.webdriver.common.mobileby import MobileBy

from Appium_Demo.appium_pageObj.page.BasePage import BasePage
from Appium_Demo.appium_pageObj.page.ContactEdit_Page import ContactEdit


class ContactDetailSetting(BasePage):

    def edit_profile(self):
        #进入个人信息编辑页，进行删除和其他编辑操作
        self.find_and_click(MobileBy.XPATH,'//*[@text="编辑成员"]')
        return ContactEdit(self.driver)