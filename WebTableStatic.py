import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


obj_serv = Service("C:\\Users\\ossmarkovic\\Desktop\\Projects\\!Selenium\\chromedriver.exe")
url = "https://testautomationpractice.blogspot.com/"
driver = webdriver.Chrome(service=obj_serv)
driver.maximize_window()
driver.get(url)

# 1. count number of rows and columns
numb_rows = driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr")
print("Number of row: ",len(numb_rows))#7
numb_columns = driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr[1]/th")
print("Number of columns: ",len(numb_columns)) #4

# 2. read specific row and column data ==> row 5 column 1 = Master In Selenium
data = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[5]/td[1]").text
print(data)
"""
# 3. read all the rowa and columns data. in xpath use sintaks ["+str(ro)+"] not this [ro], dosenot work
for ro in range(2,len(numb_rows)+1):
    for co in range(1,len(numb_columns)+1):
        data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(ro)+"]/td["+str(co)+"]").text
        print(data,end="          ")
    print()
"""
# 4. Read data based on condition(list books name whose is Mukech)
for ro in range(2,len(numb_rows)+1):
    Auther_name = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(ro)+"]/td[2]").text
    if Auther_name == "Mukech":
        Name_book =  driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(ro)+"]/td[1]").text
        price_book =  driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(ro)+"]/td[4]").text
        print(Auther_name,"    ",Name_book,"   ",price_book)



