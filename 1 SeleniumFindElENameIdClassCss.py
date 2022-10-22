from selenium import webdriver                   # For starting browser
from selenium.webdriver.common.keys import Keys  # for use any key like ENTER...
from selenium.webdriver.common.by import By      # BY ACCESS TO ELEMENT IN SITE
import time

url ="http://www.python.org"
driver = webdriver.Chrome()
driver.get("http://www.python.org")

assert "Python" in driver.title
# way to assert this element in site if not title than assert error in line 16

############ 4 ways to access element search ###############################
#elem = driver.find_element(By.NAME, "q")
# 1 element = search ==> By.Name "q"
#elem1 = driver.find_element(By.CLASS_NAME,"search-field")
# 2 access the elemnet with class name
#elem2 =driver.find_element(By.CSS_SELECTOR, "#id-search-field")
# 3 access the element with  css selector

elem3 = driver.find_element(By.ID, "id-search-field")
# 4 access the element with id
elem3.clear()
elem3.send_keys("pycon")
#write what you search
elem3.send_keys(Keys.RETURN)
# after write press enter

assert "No results found." not in driver.page_source
time.sleep(5)
#driver.close()
