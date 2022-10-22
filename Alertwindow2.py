import requests
from selenium import webdriver
from selenium.common import ElementNotSelectableException, ElementNotVisibleException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


obj_serv = Service("chromedriver.exe")
url = "https://mypage.rediff.com/"
driver = webdriver.Chrome(service=obj_serv)
driver.maximize_window()
driver.get(url)
driver.find_element(By.XPATH,"//input[@value=' Go ']").click()
time.sleep(15)
alert_win = driver.switch_to.alert
print(alert_win.text)
alert_win.accept()
time.sleep(15)