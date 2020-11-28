# 一/ 在AdressList_Page中封装以下新方法：
import pytest
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Web.wework_demo.Pages.BasePage import BasePage


def scroll_to_find_member(self, name):
    # 滚动查找目标人员并点击进入详情页面
    try:
        self.find_by_scroll(name).click()
    except Exception:
        print("无法查找到该页面元素")
        return False
    return ContactDetailBriefInfoProfile(self.driver)


def find_contact(self, name):
    # 删除人员，返回通讯录页面后，等待页面刷新删除后的通讯录名单
    locator = (MobileBy.XPATH, f'//*[@text="{name}"]')
    result = WebDriverWait(self.driver, 10).until(
        expected_conditions.invisibility_of_element_located(locator))
    return result


# 二/新增ContactDetailBriefInfoProfile_Page.py模块
class ContactDetailBriefInfoProfile(BasePage):
    def enter_detail_setting(self):
        '''点击右上角编辑图标，进入用户编辑页'''
        self.find_and_click(MobileBy.XPATH, '//android.widget.TextView[@resource-id="com.tencent.wework:id/guk"]')
        return ContactDetailSetting(self.driver)


# 三/新增ContactDetailSetting.py模块
class ContactDetailSetting(BasePage):
    def edit_profile(self):
        # 进入个人信息编辑页，进行删除和其他编辑操作
        self.find_and_click(MobileBy.XPATH, '//*[@text="编辑成员"]')
        return ContactEdit(self.driver)


# 四/新增ContactEdit.py模块
class ContactEdit(BasePage):
    def contact_delete(self):
        # 找到对应删除按钮，点击删除
        print(self.driver.contexts)
        self.find_and_click(MobileBy.XPATH, '//*[@text="删除成员"]')
        print(self.driver.contexts)
        # 在弹窗中点击确认
        self.find_and_click(MobileBy.XPATH, '//*[@text="确定"]')
        # 人员删除成功后，会返回到通讯录页面
        from Appium_Demo.appium_pageObj.page.AddressList_page import AdressListPage
        return AdressListPage(self.driver)

    # 五/测试用例testcases
    @pytest.mark.run(order=1)
    def test_contact_add(self):
        # 在这里可以使用mainpage中的方法，前往通讯录页面
        name = "Hogwarts_007"
        gender = "男"
        phonenum = "13500000007"
        result = self.main.goto_Adresslist().click_addMember().addMember_Manual().add_member(name, gender,
                                                                                             phonenum).get_toast()
        assert "添加成功" == result

    @pytest.mark.run(order=2)
    def test_contact_delete(self):
        name = "Hogwarts_007"
        result = self.main.goto_Adresslist(). \
            scroll_to_find_member(name). \
            enter_detail_setting().edit_profile(). \
            contact_delete().find_contact(name)
        assert result is True
