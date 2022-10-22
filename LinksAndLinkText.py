from selenium import webdriver
from selenium.common import ElementNotSelectableException, ElementNotVisibleException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


obj_serv = Service("chromedriver.exe")
url = "https://www.nopcommerce.com/en/demo"
driver = webdriver.Chrome(service=obj_serv)



driver.maximize_window()
driver.get(url)

#click on link
#driver.find_element(By.LINK_TEXT,"Get started").click()
#driver.find_element(By.PARTIAL_LINK_TEXT,"Get").click()

# find all links in page
#links = driver.find_elements(By.TAG_NAME,"a") 84
links = driver.find_elements(By.XPATH,"//a")
print("number of links in page ",len(links))
#print name link
for link in links:
    print("name of link: ",link.text)




#driver.quit()
