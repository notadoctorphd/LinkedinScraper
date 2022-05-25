from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def login():
    
    username = #this is where your username
    password = # password

    PATH = "/usr/bin/chromedriver"
    driver = webdriver.Chrome(PATH)

    driver.get('https://www.linkedin.com')
    print(driver.title)
 
    #find elem username/email and send username
    email = driver.find_element_by_id("session_key")
    email.send_keys(username) #
 

    #find elm passowrd and send password
    password = driver.find_element_by_id("session_password")
    password.send_keys(password)
    password.send_keys(Keys.RETURN)

    time.sleep(5)

    signin = driver.find_element_by_class_name("sign-in-form__submit-button")
    signin.click()



  #  driver.quit()
login()



# 
# try:
    # main = WebDriverWait(driver, 10).until(
        # EC.presence_of_element_located((By.ID, "main"))
    # )
# 
# except:
    # driver.quit()
# 
# print(main.text)
