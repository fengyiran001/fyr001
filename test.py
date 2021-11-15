from appium import webdriver
import time


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10.0'
desired_caps['deviceName'] = 'huaweip50pro'
desired_caps['appPackage'] = 'com.xunmeng.pinduoduo'
desired_caps['appActivity'] = '.ui.activity.MainFrameActivity'
desired_caps['udid'] = 'SED0221722001702'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.find_element_by_name("1").click()

driver.find_element_by_name("1").click()
