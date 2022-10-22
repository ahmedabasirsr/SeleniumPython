from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

url = "https://opensource-demo.orangehrmlive.com"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
time.sleep(5) #wait time to view element 
ele_user = driver.find_element(By.NAME,"username")
ele_user.send_keys("Admin")
ele_pass = driver.find_element(By.NAME,"password")
ele_pass.send_keys("admin123")
ele_log = driver.find_element(By.CSS_SELECTOR,".oxd-form-actions.orangehrm-login-action")
ele_log.click()







