from selenium import webdriver
from time import sleep


class TestForm:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_form_submit(self):
        url = "https://testerhome.com/account/sign_in"
        self.driver.get(url)
        name_element = self.driver.find_element_by_id("user_login")
        passwd_element = self.driver.find_element_by_id("user_password")
        submit_element = self.driver.find_element_by_name("commit")

        name_element.send_keys("username")
        print(name_element.get_attribute("value"))
        passwd_element.send_keys("123456")
        print(passwd_element.get_attribute("value"))
        submit_element.click()
        sleep(3)




