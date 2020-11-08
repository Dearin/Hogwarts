from Appium_Demo.frame_demo.Pages.MainPage import MainPage


class TestBlackList:

    def test_goto_search(self):
        self.main = MainPage()
        self.main.goto_market().goto_search()