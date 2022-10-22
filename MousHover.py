from selenium import webdriver
#from selenium.webdriver.common import ActionChains #1
#from selenium.webdriver.common.action_chains import ActionChains #2import
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

obj_serv = Service("C:\\Users\\ossmarkovic\\Desktop\\Projects\\!Selenium\\chromedriver.exe")
url = "https://verifysoft.com/en_ctcpp.html"
driver = webdriver.Chrome(service=obj_serv)
driver.maximize_window()
driver.get(url)

about = driver.find_element(By.XPATH,"//a[contains(text(),'About')]")
comp = driver.find_element((By.XPATH,"/html[1]/body[1]/div[1]/nav[1]/ul[1]/li[2]/ul[1]/li[5]/a[1]")




#Actions mouse

act = ActionChains(driver)


act= act.move_to_element(about).move_to_element(comp).click().perform()