
'''
添加成员页面
'''
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Appium_Demo.appium_pageObj.page.BasePage import BasePage


class ContactAdd(BasePage):
    def add_member(self, name, gender, phonenum):
        # 定位name,并输入用户姓名
        self.find(MobileBy.XPATH,
                  "//*[contains(@text, '姓名')]/../*[@text='必填']").send_keys(name)
        self.find(MobileBy.XPATH, "//*[contains(@text, '性别')]/..//*[@text='男']").click()
        # 设置性别
        if gender == "男":
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element(MobileBy.XPATH, "//*[@text='女']"))
            self.find(MobileBy.XPATH, "//*[@text='男']").click()
        else:
            self.find(MobileBy.XPATH, "//*[@text='女']").click()
        # 设置电话号码
        self.find(MobileBy.XPATH,
                  '//*[contains(@text, "手机") and contains(@class, "TextView")]/..//android.widget.EditText').send_keys(
            phonenum)

        # 点击保存,设置一个显性等待
        self.find(MobileBy.XPATH, "//*[@text='保存']").click()

        # 点击保存后会返回到手动添加成员的页面
        from Appium_Demo.appium_pageObj.page.MemberInviteMenu_Page import MemberInviteMenuPage
        return MemberInviteMenuPage(self.driver)
