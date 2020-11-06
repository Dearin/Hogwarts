import shelve
from time import sleep

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestImport:

    def setup_method(self, method):
        options = Options()
        options.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(5)

    def teardown_method(self, method):
        self.driver.quit()

    def test_wework_import(self):
        # 使用cookies绕过登陆，cookies.db中的cookie,失效了需要及时更新的，
        # cookies = self.driver.get_cookies()
        db = shelve.open("cookies")
        # db['cookie'] = cookies
        cookies = db['cookie']
        db.close()
        # 访问页面并注入cookie
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # 注入cookies
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()

        # # 点击通讯录,进入通讯录
        # WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,'#menu_contacts')))
        # self.driver.find_element(By.CSS_SELECTOR,'#menu_contacts').click()

        # 在首页点击导入联系人
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
        sleep(2)

        # 点击文件导入上传文件,send_keys中使用文件路径即可
        self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_uploadInputMask").send_keys('/Users/deng/Downloads/人短表信息导入模板.xls')
        sleep(2)

        # 验证文件是否上传成功
        filename = self.driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div[2]/div[1]/div[2]').text
        assert "人短表信息导入模板" in filename
