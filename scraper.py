from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import pandas as pd
import time
class Scraper:

    global username, password, PATH, driver  
    username ="********"   # input("Type Username: ")
    password ="********"  # input("Type Password: ")              
    PATH = "/usr/bin/chromedriver"
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')  # Last I checked this was necessary.
    driver = webdriver.Chrome(PATH, chrome_options=options)
    
    def __init__(self):
        pass          

    
    def login(self, username, password):

        self.username = username
        self.password = password

        driver.get('https://www.linkedin.com')
             
        #find elem username/email and send username
        email = driver.find_element_by_id("session_key")
        print(driver.title)
        print(driver.title + " is loading............. Preparing to pass email to linkedin")
        email.send_keys(username) 
        #find elm passoswrd and send password
        passwrd = driver.find_element_by_id("session_password")
        passwrd.send_keys(password)

        time.sleep(5)

        print('login was successful')
        signin = driver.find_element_by_class_name("sign-in-form__submit-button")
        signin.click()

    
      
    global search_job, search_location #should set global variable for search_job and should i
    search_job = "Recruiter"  # input("Search by title, skill, or company: ")
    search_location = "Denver"  # input("Enter location: ")
    # search_location = search_location.replace(", ", "%2C%20")
    # search_location = cg.onelineaddress(search_location)
    # location=Denver%2C%20Colorado%2C%20United%20States

    def job_scrapes(self):
        # https://www.linkedin.com/jobs/search/?geoId=103644278&keywords=Recruit&location=United%20States
        site_linkedin = str(("https://www.linkedin.com/jobs/search/?geoId=103644278&keywords=" + search_job))
        driver.get(site_linkedin)
        print(driver.title)
        time.sleep(3)
        # job_search = driver.find_element_by_id("jobs-search-box-keyword-id-ember30")
        # job_search.double_click()
        # time.sleep(3)
        # Scraper.cleartext(job_search)
        # job_search.send_keys(search_job)
        # 
        print('job scraping has commenced ... ... ... .. \n Please wait .. .. .. ')
  # //*[@id="jobs-search-box-location-id-ember30"]
     # 
        job_location = driver.find_element_by_xpath("//*[contains(@id, 'jobs-search-box-location-id-ember')]")
        #//*[@id="jobs-search-box-location-id-ember30"]
        # job_location.click()
        time.sleep(3)
        job_location.clear()
        time.sleep(3)
        job_location.send_keys(search_location)
        time.sleep(3)
        job_location.send_keys(Keys.RETURN)

        print('locatin element ... ... ... ')

        details = driver.find_elements_by_xpath("//*[contains(@id,'job-details')]")
        ##job-details > span > p:nth-child(3)
        time.sleep(5)
        details_text = details.text
        print(details_text)  
        
        



         
        # button_search = driver.find_element_by_xpath("/html/body/div[5]/header/div/div/div/div[2]/button[1]")
        # button_search.click()
       # # else:
            # # job_location.send_keys(search_job)
            # 


Scraper.login(Scraper, username, password)
Scraper.job_scrapes(Scraper)
    

if __name__ == "__main__":
    Scraper.login(Scraper, username, password)
    Scraper.job_scrapes(Scraper)
    
# 
# print(main.text)
