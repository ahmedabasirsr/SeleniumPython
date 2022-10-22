from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
obj_serv = Service("C:\\Users\\Nastavnik\\Desktop\Projects\\!Selenium\\chromedriver.exe")
url = "http://automationpractice.com/index.php"
driver = webdriver.Chrome(service=obj_serv)
driver.maximize_window()
driver.get(url)

#Relative Xpath  with contains and starts-with
driver.find_element(By.XPATH,"//input[contains(@id,'search_query_top')]").send_keys("T-shirts")
driver.find_element(By.XPATH,"//button[starts-with(@name,'submit')]").click()










