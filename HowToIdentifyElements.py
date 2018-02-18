"""
There are 8 different methods to identify elements in the HTML page based on DOM structure.
1. id
2. name
3. link text
4. x-path
5. CSS selector
6. class name
7. tag name
8. partial link text

Note:
CSS and X-Path methods are used when other options are not available, but these are very powerful.
Tag Name is usually not used because it will match multiple elements.

Element Identification:
Element identification happens using the HTML tag, properties and values of the elements.
To identify any element, we should be able to inspect the source of the element.
Every browser provides an inbuilt tool by default which can be used for element source identification.
In FireFox we can use a tool(add-on) called fire bug instead of default inspector.
"""
from selenium import webdriver
path = "F:\\Python_Automation\\drivers\\geckodriver.exe"
driver = webdriver.Firefox(executable_path=path)
driver.get("https://www.amazon.com/")
driver.implicitly_wait(5)
# Identify Element by ID
driver.find_element_by_id("nav-link-accountList").click()
print(driver.current_window_handle)
# Identify Element by name
driver.find_element_by_name("email").send_keys("This_was_identified_by_name_property")
# Identify Element by class name
driver.find_element_by_class_name("a-button-input").click()
# Identify Element by link text
driver.find_element_by_link_text("Conditions of Use").click()
driver.switch_to.window("4294967297")
print("Test This Line..")
driver.get("http://help.websiteos.com/websiteos/example_of_a_simple_html_page.htm")
print(driver.find_element_by_tag_name('h1').text)  # to get the contents of the html tag
driver.get("https://www.google.com/gmail/about/#")
# Identify Element by partial link text
driver.find_element_by_partial_link_text("Create").click()
driver.close()
driver.quit()
