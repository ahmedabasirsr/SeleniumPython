import requests
from selenium import webdriver
from selenium.common import ElementNotSelectableException, ElementNotVisibleException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


obj_serv = Service("chromedriver.exe")
url = "https://the-internet.herokuapp.com/javascript_alerts"
driver = webdriver.Chrome(service=obj_serv)
driver.maximize_window()
driver.get(url)
driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()
time.sleep(15)
#alert_window is content of window alert
alert_window = driver.switch_to.alert
# print text on window alert
print(alert_window.text)
# send text on filied text
alert_window.send_keys("Welcom")
# press ok on window alert
#alert_window.accept()
#press cancel on alert window
alert_window.dismiss()
time.sleep(15)
