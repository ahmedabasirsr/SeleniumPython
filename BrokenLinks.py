import requests
from selenium import webdriver
from selenium.common import ElementNotSelectableException, ElementNotVisibleException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


obj_serv = Service("chromedriver.exe")
url = "http://www.deadlinkcity.com/"
driver = webdriver.Chrome(service=obj_serv)



driver.maximize_window()
driver.get(url)

#click on broken link
broken_links = driver.find_elements(By.TAG_NAME,"a")
count = 0
for link in broken_links:
    urll = link.get_attribute("href")
    try:
        req = requests.head(urll)
    except:
        None
    if req.status_code>=400:
        print(urll,"the link is proken")
        count +=1
    else:
        print(urll," the link is valid")
print("the total number broken link: ",count)







#driver.quit()
