from appium import webdriver
from time import sleep
# 这里其实一种新的编码的方式来进行初始化的基本的参数设计
desire_cap = {}
desire_cap["platformName"] = "android"
desire_cap["deviceName"] = "emulator-5554"
desire_cap["appPackage"] = "com.xueqiu.android"
desire_cap["appActivity"] = "com.xueqiu.android.common.MainActivity"
desire_cap["noReset"] = "true" # 这里就避免来每次打开弹出的同意窗口
desire_cap["dontStopAppOnReset"] = 'true'
desire_cap["skipDeviceInitialization"] = 'true'

# 初始化driver
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desire_cap)
driver.implicitly_wait(5)
# 进行页面元素定位
search_ele = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
search_ele.click()
input_ele = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
driver.implicitly_wait(3)
input_ele.send_keys("alibabab")
input_ele.click()
sleep(3)


