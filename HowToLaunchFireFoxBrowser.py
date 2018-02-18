from selenium import webdriver
path = "F:\\Python_Automation\\drivers\\geckodriver.exe"
driver = webdriver.Firefox(executable_path=path)
driver.get("https://www.amazon.com/Amazon-Student/b?ie=UTF8&node=668781011")
driver.maximize_window()
driver.set_page_load_timeout(30)
driver.close()

