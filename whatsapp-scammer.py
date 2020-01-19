from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
import time

driver=webdriver.Chrome("C:\WebDrivers\chromedriver")
driver.get("https://web.whatsapp.com/")

wait=WebDriverWait(driver,600)

target='"Notes"' #enter your targets name
string="Heya!!!"   #enter you message

x_arg='//span[contains(@title,'+ target +')]'
target=wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
target.click()
input_box=driver.find_element_by_class_name('_13mgZ')

for i in range(200):    #enter no of message you want to send.
    input_box.send_keys(string+Keys.ENTER)
