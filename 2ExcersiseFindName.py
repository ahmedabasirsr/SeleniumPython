from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

url = "https://demo.guru99.com/test/newtours/"
driver = webdriver.Chrome()
driver.get(url)
#print(driver.title)
# Title of site
#print(driver.current_url)
# Link of site
#flight = driver.find_elements(By.CLASS_NAME,"mouseOut")[1].click()
#list flight has elements===> Home, Flight, Hotels ...
time.sleep(3)
ele_useName = driver.find_element(By.NAME,"userName").send_keys("userName")
ele_passowrd = driver.find_element(By.NAME,"password").send_keys("password")
ele_submit = driver.find_element(By.NAME,"submit").click()





#time.sleep(3)
# sotp next lin 3 second
#driver.close()
# close current browser
#driver.quit()
# close all browsrs
