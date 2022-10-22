from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
obj_serv = Service("chromedriver.exe")
url = "https://money.rediff.com/gainers"
driver = webdriver.Chrome(service=obj_serv)
driver.maximize_window()
driver.get(url)
"""
#ancestor element
ancestor=driver.find_element(By.XPATH,"//tbody/tr/td/a/ancestor::tr ")
print(ancestor.text)
"""
#descendant element for this does not has descedant, thats whay use ancestor
descendants = driver.find_elements(By.XPATH,"//tbody/tr[11]/td[1]/a[1]/ancestor::tr/descendant::* ")
print("Number of descedants nods",len(descendants))
print("Number of descedants nods",descendants[2].text)







