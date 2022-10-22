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
""" //*[#@id="leftcontainer"]/table/tbody/tr[1]/td[2] 8985
jijec = driver.find_elements(By.XPATH,"//*[@id='leftcontainer']/table/tbody/tr/td")
print(jijec[5].text)
#print(len(jijec))
"""
"""
#self ==> relative xpath/self::tagname == //tbody/tr[10]/td[1]/a[1]/self::a
name_f=driver.find_element(By.XPATH,"//tbody/tr[10]/td[1]/a[1]/self::a ")
print("Name of company(self ele.) ",name_f.text)

name_f=driver.find_elements(By.XPATH,"//tbody/tr/td/a/self::a ") #total links=1340 neto=1293
#print(len(name_f))
print(name_f[1293].text)

#parent element, you will have same value because parent element it dosent value
name_f=driver.find_element(By.XPATH,"//tbody/tr[10]/td[1]/a[1]/parent::td ")
print("Name of company(self ele.) ",name_f.text)

#child element of self does not has childوThat's why we have to go back to the ancestor
childs=driver.find_elements(By.XPATH,"//tbody/tr[10]/td[1]/a[1]/ancestor::tr/child::td ")
print("Name of company(child ele.) ",len(childs))
print(childs[1].text,childs[4].text) # 5 elentents
"""
childs=driver.find_elements(By.XPATH,"//tbody/tr/td/a/ancestor::tr/child::td ")
print("Name of company(child ele.) ",len(childs)) # 6475 elements
print(childs[0].text,childs[1].text,childs[2].text,childs[3].text,childs[4].text)








