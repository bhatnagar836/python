from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_binary
from selenium.webdriver.chrome.options import Options
from getpass import getpass

chrome_options = Options()
# username=input("jahnvijahnvi2@in.com")
# password= getpass("studies")


# chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
# chrome_options.add_experimental_option('useAutomationExtension', False)
# chrome_options.add_argument("--disable-blink-features=AutomationControlled") # To hide Automation
# chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])



driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://www.facebook.com/")
driver.find_element_by_name("email").send_keys("jahnvijahnvi2@in.com")
driver.find_element_by_name("pass").send_keys("studies")

# username_textbox= driver.find_element_by_id("email")
# username_textbox.send_keys("username")
# password_textbox= driver.find_element_by_id("pass")
# password_textbox.send_keys("password")
login_button=driver.find_element_by_name("login")
login_button.submit()