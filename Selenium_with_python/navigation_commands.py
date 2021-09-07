from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_binary
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://www.facebook.com/")
print(driver.title)

driver.get("https://www.codewithharry.com/")
time.sleep(5)
print(driver.title)

time.sleep(5)
driver.back()
print(driver.title)

time.sleep(5)
driver.forward()
print(driver.title)

