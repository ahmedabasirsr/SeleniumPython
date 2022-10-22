from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
obj_serv = Service()

url = "http://automationpractice.com/index.php"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

time.sleep(5) #wait time to view element
sliders = driver.find_elements(By.CLASS_NAME,"homeslider-container")
print(len(sliders)) # for slides elements
links = driver.find_elements(By.TAG_NAME,"a")
print(len(links))









