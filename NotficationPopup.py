import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#creat option in webdriver
ops = webdriver.ChromeOptions()
#creat what is option notification
ops.add_argument("--disable-notificatio")
obj_serv = Service("C:\\Users\\ossmarkovic\\Desktop\\Projects\\!Selenium\\chromedriver.exe")
#C:\Users\ossmarkovic\Desktop\Projects\!Selenium
url = "https://whatmylocation.com/"
# add option in webdriver
driver = webdriver.Chrome(service=obj_serv,options=ops)
driver.maximize_window()
driver.get(url)
