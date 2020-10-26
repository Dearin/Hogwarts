from selenium import webdriver
from selenium.webdriver import TouchActions, ActionChains

from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestTouchChain:
    def setup(self):
        opt = webdriver.ChromeOptions()
        opt.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=opt)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_touchchain_scrolltobuttom(self):
        '''
        1/打开chrome浏览器
        2/输入 Selenium测试 关键字，并点击搜索
        3/滑动至结果页底部
        4/点击切换下一页
        '''
        url = "https://www.baidu.com/"
        self.driver.get(url)
        element = self.driver.find_element_by_xpath('//*[@id="kw"]')
        search_element = self.driver.find_element_by_xpath('//*[@id="su"]')

        # 搜索框获取光标
        element.send_keys("Selenium测试")
        WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="su"]')
                                       )
        )
        action = TouchActions(self.driver)
        # 这个tap就是有错
        #action.tap(self.driver.find_element_by_id("su")).perform()
        ac = ActionChains(self.driver)
        ac.click(search_element).perform() # 这样就成功了
        action.scroll_from_element(element,0,10000).perform()
        sleep(3)
