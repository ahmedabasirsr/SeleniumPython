from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
obj_serv = Service()

url = "https://www.facebook.com/"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

time.sleep(5) #wait time to view element
#tag and ID ==> tagname#value of id
#driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("assddf")
#tag and class ==> tagname.vlaue of class name==> take name class to first space
driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("abc")










