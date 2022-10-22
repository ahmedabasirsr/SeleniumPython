from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
obj_serv = Service("chromedriver.exe")
url = "https://www.google.com/"
driver = webdriver.Chrome(service=obj_serv)
driver.maximize_window()
driver.get(url)
print(driver.title)
print(driver.current_url)

search_googl=driver.find_element(By.NAME,"q")
search_googl.send_keys("selenium")
search_googl.submit()
driver.find_element(By.XPATH,"//h3[normalize-space()='Selenium']").click()
driver.back()
driver.refresh()
time.sleep(5)
#driver.close()
driver.quit()
