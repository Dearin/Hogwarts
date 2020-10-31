
# 初始化一下
from appium import webdriver

desire_cap = {
  "platformName": "android",
  "deviceName": "emulator-5554",
  "appPackage": "com.xueqiu.android",
  "appActivity": ".view.WelcomeActivityAlias",
  "noReset": True # 避免重置出现初始化的弹窗
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desire_cap)
driver.implicitly_wait(3)
el1 = driver.find_element_by_id("com.xueqiu.android:id/home_search")
el1.click()
driver.implicitly_wait(10)
el2 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el2.send_keys("alibaba")
el3 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView[1]")
driver.implicitly_wait(3)
el3.click()
