import  time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

obj_serv = Service("C:\\Users\\ossmarkovic\\Desktop\\Projects\\!Selenium\\chromedriver.exe")
url = "https://www.dummyticket.com/dummy-ticket-for-visa-application/"
driver = webdriver.Chrome(service=obj_serv)
driver.get(url)
driver.maximize_window()

#sekect element filied brith date
driver.find_element(By.XPATH,"//input[@id='dob']").click()

#variable for select month element
month_picker = Select(driver.find_element(By.XPATH,"//select[@aria-label='Select month']"))
#select text for visible text
month_picker.select_by_visible_text("Oct")
# the same for select year
year_picker=Select(driver.find_element(By.XPATH,"//select[@aria-label='Select year']"))
year_picker.select_by_visible_text("1962")

time.sleep(5)
all_days = driver.find_elements(By.XPATH,"//div[@id='ui-datepicker-div']//table/tbody/tr/td/a")
for day in all_days:
    if day.text == "7":
        day.click()
        break


