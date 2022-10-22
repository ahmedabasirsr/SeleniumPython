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

#Relative Xpath  with 2 atributes == 1 or 2
driver.find_element(By.XPATH,"//input[@id='search_query_top' or@name='search_query']").send_keys("T-shirts")
driver.find_element(By.XPATH,"//button[@name='submit_search'and@type='submit']").click()










