import requests
from selenium import webdriver
from selenium.common import ElementNotSelectableException, ElementNotVisibleException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


obj_serv = Service("C:\\Users\\Nastavnik\\Desktop\\Projects\\!Selenium\\chromedriver.exe")
url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
driver = webdriver.Chrome(service=obj_serv)
driver.maximize_window()
driver.get(url)
# returne id singl window
window_id = driver.current_window_handle #CDwindow-833538693490066B52C109D0F8BA83B3
print(window_id)                         #CDwindow-528AFFF472CCA526963349E66A077E21
time.sleep(15)
driver.find_element(By.XPATH,"//a[normalize-space()='OrangeHRM, Inc']").click()
time.sleep(10)
window_ids =driver.window_handles
perant_win = window_ids[0]
child_win = window_ids[1]
print(perant_win," ",child_win)
time.sleep(15)
driver.switch_to.window(child_win)
print((driver.title))
driver.switch_to.window(perant_win)
print((driver.title))

