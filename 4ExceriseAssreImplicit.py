from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

url = "https://demo.guru99.com/test/newtours/"
driver = webdriver.Chrome()
driver.get(url)

driver.implicitly_wait(5)
# here we waite maximum 5 seconds
#print(driver.title)
assert "Welcome: Mercury Tours" in driver.title
# if it's not assert, it won't work anymore " break program AssertionError "
driver.find_element(By.NAME,"userName").send_keys("username")
driver.find_element(By.NAME,"password").send_keys("password")
driver.find_element(By.NAME,"submit").click()

#print(driver.title) aria-label
