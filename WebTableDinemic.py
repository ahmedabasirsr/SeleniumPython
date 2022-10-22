import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


obj_serv = Service("C:\\Users\\ossmarkovic\\Desktop\\Projects\\!Selenium\\chromedriver.exe")
url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
driver = webdriver.Chrome(service=obj_serv)
driver.maximize_window()
driver.get(url)

us=driver.find_element(By.XPATH,"//input[@placeholder='Username']")
time.sleep(5)
us.send_keys("ffff")



