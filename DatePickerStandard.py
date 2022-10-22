import  time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

obj_serv = Service("C:\\Users\\ossmarkovic\\Desktop\\Projects\\!Selenium\\chromedriver.exe")
url = "https://jqueryui.com/datepicker/"
driver = webdriver.Chrome(service=obj_serv)
driver.get(url)

driver.switch_to.frame(0)
#driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("05/30/2022") #momt/day/year
year = "2023"
month = "June"
date = "7"

driver.find_element(By.XPATH,"//input[@id='datepicker']").click()
while True:
    mon = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    yea = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text
    if mon == month and year == yea :
        break
    else:
        driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/a[2]/span").click()

driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/table/tbody/tr[2]/td[4]/a").click()

