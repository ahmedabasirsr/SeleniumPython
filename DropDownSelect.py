import requests
from selenium import webdriver
from selenium.common import ElementNotSelectableException, ElementNotVisibleException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.support.select import Select

obj_serv = Service("chromedriver.exe")
url = "https://www.opencart.com/index.php?route=account/register"
driver = webdriver.Chrome(service=obj_serv)



driver.maximize_window()
driver.get(url)
#drop_country = driver.find_element(By.XPATH,"//select[@id='input-country']")
drop_country = Select(driver.find_element(By.XPATH,"//select[@id='input-country']"))

#drop_country.select_by_visible_text("Iraq")
#drop_country.select_by_value("95")
#drop_country.select_by_index(100)

#captur all options and print them
alloptions = drop_country.options
print("Total number of options: ",len(alloptions))
#for op in alloptions:
 #   print(op.text)

#select option without useing built in method
for op in alloptions:
    if op.text == "Iraq":
        op.click
        break



