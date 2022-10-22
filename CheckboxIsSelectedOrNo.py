from selenium import webdriver
from selenium.common import ElementNotSelectableException, ElementNotVisibleException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


obj_serv = Service("chromedriver.exe")
url = "https://itera-qa.azurewebsites.net/home/automation/"
driver = webdriver.Chrome(service=obj_serv)



driver.maximize_window()
driver.get(url)
#Select 1 checkbox
#driver.find_element(By.XPATH,"//input[@id='monday']").click()
#Select all checkboxs
check_boxs = driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
print(len(check_boxs))
check_boxs[-1].click()
check_boxs[-2].click()
#for check in check_boxs:
 #   check.click()
'''
for chekbox in check_boxs:
    day = chekbox.get_attribute("id")
    if day == "monday" or day == "friday" :
        chekbox.click()
'''
time.sleep(5)
for checkbox in check_boxs:
    if checkbox.is_selected():
        checkbox.click()


#driver.quit()
