from selenium import webdriver
from selenium.common import ElementNotSelectableException, ElementNotVisibleException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


obj_serv = Service("C:\\Users\\Nastavnik\\Desktop\\Projects\\!Selenium\\chromedriver.exe")
url = "https://demo.automationtesting.in/Frames.html"
driver = webdriver.Chrome(service=obj_serv)
driver.maximize_window()
driver.get(url)
#driver.switch_to()
driver.find_element(By.XPATH,"//a[normalize-space()='Iframe with in an Iframe']").click()
# first you most to go in parent frame(outer)
parent_frame = driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")
# second most to go in inner frame(into frame) like element webdriver
inner_frame = driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(inner_frame)
#this element now you can access it
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("Hello")
# direct returne on parent frame only youcan that but here i donot nothing
#driver.switch_to.parent_frame()