import requests
from selenium import webdriver
from selenium.common import ElementNotSelectableException, ElementNotVisibleException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


obj_serv = Service("chromedriver.exe")
#url = "https://the-internet.herokuapp.com/basic_auth"
driver = webdriver.Chrome(service=obj_serv)
driver.maximize_window()
#bybus user name and passowrd in url adress exp: admin:admin@adress site
url = "https://admin:admin@the-internet.herokuapp.com/basic_auth"
driver.get(url)
time.sleep(10)
