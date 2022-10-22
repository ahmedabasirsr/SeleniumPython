import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

obj_serv = Service("C:\\Users\\ossmarkovic\\Desktop\\Projects\\!Selenium\\chromedriver.exe")
#C:\Users\ossmarkovic\Desktop\Projects\!Selenium
url = "https://poslovi.infostud.com/"
driver = webdriver.Chrome(service=obj_serv)
driver.maximize_window()
driver.get(url)

pos_work = driver.find_element(By.XPATH,"//input[@id='q']")
pos_work.send_keys("it")
pos_work.submit()
time.sleep(5)
job_titl = driver.find_elements(By.XPATH,"")
print(len(job_titl))

