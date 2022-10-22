from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
obj_serv = Service()

url = "https://demo.nopcommerce.com/"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

time.sleep(5) #wait time to view element 

#link tekxt and partial text
#driver.find_element(By.LINK_TEXT,"Register").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"ist").click()







