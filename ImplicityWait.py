from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
obj_serv = Service("chromedriver.exe")
url = "https://www.google.com/"
driver = webdriver.Chrome(service=obj_serv)
# maximum tim to wait whole code
driver.implicitly_wait(10)

driver.maximize_window()
driver.get(url)

search_googl=driver.find_element(By.NAME,"q")
search_googl.send_keys("selenium")
search_googl.submit()
driver.find_element(By.XPATH,"//h3[text()='Selenium']").click()

driver.quit()
