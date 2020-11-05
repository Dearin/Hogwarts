import pytest

from Appium_Demo.appium_pageObj.page.App_index import App_Index
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

class TestContact:

    def setup(self):
  #一般用例在这进行driver的初始化，但是考虑的PO设计
  # 此处需要如下操作：
        # 实例化App_Index对象
        self.app = App_Index()
        # 链式调用，调用app中的start方法完成应用启动，
        #再掉用goto_main的方法来实现前往主页，并使用main的所有方法
        self.main = self.app.start_app().goto_main()


    def teardown(self):
        self.app.stop_app()

    @pytest.mark.run(order=1)
    def test_contact_add(self):
        # 在这里可以使用mainpage中的方法，前往通讯录页面
        name = "Hogwarts_007"
        gender = "男"
        phonenum ="13500000007"
        result = self.main.goto_Adresslist().click_addMember().addMember_Manual().add_member(name, gender, phonenum).get_toast()
        assert "添加成功" == result


    @pytest.mark.run(order=2)
    def test_contact_delete(self):
        name = "Hogwarts_007"
        result = self.main.goto_Adresslist().\
                     scroll_to_find_member(name).\
                     enter_detail_setting().edit_profile().\
                     contact_delete().find_contact(name)
        assert result is True
