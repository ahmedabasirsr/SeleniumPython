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

#Absolutely Xpath == full xpath
'''
driver.find_element(By.XPATH,"/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/input[4]").send_keys("T-shirt")
driver.find_element(By.XPATH,"/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/button").click()
'''
#relative Xpath == xpath
driver.find_element(By.XPATH,"//*[@id='search_query_top']").send_keys("T-shirt")
driver.find_element(By.XPATH,"//*[@id='searchbox']/button").click()













