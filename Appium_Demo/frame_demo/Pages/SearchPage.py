from selenium.webdriver.common.by import By

from Appium_Demo.frame_demo.Pages.BasePage import BasePage


class SearchPage(BasePage):
    def search(self):
        path ='../yamls/search.yaml'
        func_name ='search'
        self.yaml_parse(path,func_name)

        ele = self.find(By.XPATH,'//android.widget.TextView[@text="阿里巴巴"]')
        return ele.text
