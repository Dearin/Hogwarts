
# Selenium测试用例编写要点
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class TestHogwarts:

    '''做一些资源的初始化'''
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # 一般在这里可以设置隐式等待，伴随整个driver生命周期。

    '''做close'''
    def teardowan(self):
        self.driver.quit()

    '''进行测试用例'''
    '''进入testerhome,点击精华帖的第一条'''
    def test_hogwarts(self):
        url = "https://testerhome.com/"
        self.driver.get(url)
        # 点击社区,添加显式等待，等待"社区"按钮可点击的时候，进行点击
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="main-nav-menu"]/ul/li[1]/a')))
        self.driver.find_element_by_xpath('//*[@id="main-nav-menu"]/ul/li[1]/a').click()

        # 上面这样写，真的好臭长哦
        print("Hello")
       # self.driver.find_element_by_css_selector("#main-nav-menu > ul > li:nth-child(1) > a").click()



