from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_binary
from selenium.webdriver.chrome.options import Options


chrome_options = Options()


# chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
# chrome_options.add_experimental_option('useAutomationExtension', False)
# chrome_options.add_argument("--disable-blink-features=AutomationControlled") # To hide Automation
# chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://www.facebook.com/")
print(driver.title)
print(driver.current_url)
print(driver.page_source)
driver.close()

