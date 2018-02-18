from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
path = "F:\\Python_Automation\\drivers\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)
driver.get("https://www.amazon.com/Amazon-Student/b?ie=UTF8&node=668781011")
driver.maximize_window()
driver.set_page_load_timeout(30)
driver.close()
