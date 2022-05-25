from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from secrets import username, password

class Scraper:

    def __init__(self):
        pass          
    
    def login(self, username, password):

        self.username = username
        self.password = password

        print("Enter your credentials : \n ")
         
        username = input("Enter your username: ")
        password = input("Enter you password: ")
            
        # username = secrets.username  #this is where your username
        # password = secrets.password
           
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
Scraper.login(Scraper, username, password)



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
