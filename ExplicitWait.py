from selenium import webdriver
from selenium.common import ElementNotSelectableException, ElementNotVisibleException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

obj_serv = Service("chromedriver.exe")
url = "https://www.google.com/"
driver = webdriver.Chrome(service=obj_serv)
#declration for exciplit wait, max time 10 seconds but with poll_frequency=2 may bi wait time is reduce
class NoSuchEementException:
    pass


mywait = WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[NoSuchEementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException,
                                                     Exception]
                       )


driver.maximize_window()
driver.get(url)

search_googl=driver.find_element(By.NAME,"q")
search_googl.send_keys("selenium")
search_googl.submit()
search_element = mywait.until(EC.presence_of_element_located((By.XPATH,"//h3[text()='Selenium']")))
search_element.click()

driver.quit()
