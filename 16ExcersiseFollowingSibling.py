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

#Fllowing element for this does not has Fllowing, thats whay use ancestor
followings = driver.find_elements(By.XPATH,"//tbody/tr[11]/td[1]/a[1]/ancestor::tr/following::* ")
print("Number of descedants nods",len(followings))
#print("Number of Fllowing nods",fllowings[2].text) //tbody/tr[38]/td[1]/a[1]/ancestor::tr/following::* 17883
"""
#Fllowing-siblings element
following_siblings = driver.find_elements(By.XPATH,"//tbody/tr[11]/td[1]/a[1]/ancestor::tr/following-sibling::* ")
print("Number of following_siblings nods",len(following_siblings))





