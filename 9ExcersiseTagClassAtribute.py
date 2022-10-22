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
#tag name and atributes ==> tagname[atribute=value]==> input[data-testid=royal_email] witout ""
#driver.find_element(By.CSS_SELECTOR,"input[data-testid=royal_email]").send_keys("abc")
#tag name,class and atribute==> tagname.vlaueclass[atribute=value] without "" in atribute
driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal_email]").send_keys("abc")
driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal_pass]").send_keys("abc")











