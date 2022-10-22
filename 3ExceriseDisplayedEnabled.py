from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

url = "https://www.expedia.com/"
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
time.sleep(5)
ele = driver.find_elements(By.CLASS_NAME,"uitk-tab")
#list ele has contient of 6 ele(stay, flight, ...)
#print(ele[1].is_displayed())
#true if this ele view in display
#print(ele[1].is_enabled())
#true if this ele is enabled
#print(ele[1].is_selected())
ele[1].click()