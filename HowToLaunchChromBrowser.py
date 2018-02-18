"""
Problem: Windows Defender opens tab on Chrome with message "Windows Defender wants to reset your settings" each time
Chrome browser is started.  This tab opens in addition to any homepage tabs.

This problem is caused by a key in the registry with the name, "TriggeredReset".
The solution is to Rename the "TriggeredReset" folder to "TriggeredReset_1"
"""
from selenium import webdriver
path = "F:\\Python_Automation\\drivers\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
driver.get("https://www.amazon.com/Amazon-Student/b?ie=UTF8&node=668781011")
driver.maximize_window()
driver.set_page_load_timeout(30)
driver.close()
