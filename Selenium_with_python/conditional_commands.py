from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_binary
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://www.facebook.com/")

user_ele= driver.find_element_by_name("email").send_keys("jahnvijahnvi2@in.com")
print(user_ele.is_displayed()) #returns true/false based on whether element is displayed or not
print(user_ele.is_enabled()) #returns true/false based on whether element is enabled or not

pass_ele= driver.find_element_by_name("pass").send_keys("studies")
print(pass_ele.is_displayed())
print(pass_ele.is_enabled())

login_button=driver.find_element_by_name("login")
login_button.submit()
