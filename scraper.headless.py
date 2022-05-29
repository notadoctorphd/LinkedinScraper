from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import PySimpleGUI as sg
import pandas as pd
from tkinter import *
from tkinter import ttk
import time




# window.mainloop()

class Scraper:  

    global username, password, PATH, driver, options
    username = "*********"   # input("Type Username: ")
    password = "*******"  # input("Type Password: ")

    PATH = "/usr/bin/chromedriver"

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')  # Last I checked this was necessary.
    options.add_argument("--window-size=1920,1080")

    # driver = webdriver.Chrome(PATH) # , chrome_options=options)
    driver = webdriver.Chrome(PATH) # , chrome_options=options)        

            
        

    def __init__(self):
        pass
    
    # Scraper.login(Scraper, username, password)
    # Scraper.job_scrapes(Scrape

    def login(self, username, password):
            
        self.username = username
        self.password = password
        driver.get('https://www.linkedin.com')
        
# find elem username/email and send username
        email = driver.find_element_by_id("session_key")

        print(driver.title)
        print(driver.title + " is loading.....passing email to linkedin")

        email.send_keys(username)
        # find elm passoswrd and send password
        passwrd = driver.find_element_by_id("session_password")
        passwrd.send_keys(password)

        time.sleep(5)

        signin = driver.find_element_by_class_name(
            "sign-in-form__submit-button")
        signin.click()

        print('Login was Successful')

        # should set global variable for search_job and should i
        global search_job, search_location
        # input("Search by title, skill, or company: ")
        search_job = input("Search by title, skill, or company: ")
        search_location = input("Enter location: ")
        
# search_location = search_location.replace(", ", "%2C%20")
# search_location = cg.onelineaddress(search_location)
# location=Denver%2C%20Colorado%2C%20United%20States
    def job_scrapes(self):
        # https://www.linkedin.com/jobs/search/?geoId=103644278&keywords=Recruit&location=United%20States
        site_linkedin = str(
            ("https://www.linkedin.com/jobs/search/?geoId=103644278&keywords=" + search_job))
        driver.get(site_linkedin)
        print(driver.title)
        time.sleep(3)
# job_search = driver.find_element_by_id("jobs-search-box-keyword-id-ember30")
# job_search.double_click()
# time.sleep(3)
# Scraper.cleartext(job_search)
# job_search.send_keys(search_job)
#
        print('Job scraping has commenced ... ... ... .. \n Please wait .. .. .. ')
        time.sleep(3)
        job_location = driver.find_element_by_xpath(
            "//input[contains(@id, 'location')]")
# //*[@id="jobs-search-box-location-id-ember30"]
# job_location.click()
        time.sleep(3)
        job_location.clear()
        print('Scrubbing Element....')
        time.sleep(3)
        job_location.send_keys(search_location)
        print('Executing Search String..........')
        time.sleep(3)
        job_location.send_keys(Keys.RETURN)

        print('Locating Element ......... ')


        # job-details > span > p:nth-child(3)
        a = input('enter job number 1-10 : >> ')
        Xpath = f"/ /body/div[contains(@class,'application-outlet')]/div[contains(@class,'authentication-outlet')]/div[contains(@role,'main')]/div[contains(@class,'jobs-search-two-pane__wrapper')]/div[contains(@class,'jobs-search-two-pane__container grid grid__col')]/section[contains(@class,'jobs-search__left-rail')]/div[contains(@aria-label,'search results')]/div[contains(@class,'jobs-search-results display-flex flex-column')]/ul[contains(@class,'jobs-search-results__list list-style-none')]/li[1]/div[1]/div[1]"
        # Xpath = f"//*[contains(@class, 'lockup__title ember')]/div[{a}]"
        search_list = driver.find_element_by_xpath(Xpath)
        time.sleep(2)

    # //*[@id="ember635"]/div/div[1]
        searchlist = search_list.click()
        # searchlist_text = searchlist.text
        details = driver.find_element_by_xpath("//body//div//article//span[1]")
        details_text = details.text
        details_name = f"Search for {search_job} in {search_location} with selection {a}"
        print(f"Printing  details from {details_name}")
#
        # print(searchlist)
        # print(searchlist_text)
        print(details_text)
        # #//*[contains(@id,'job-details')]

        # constructor >?
    # if a  ==range(1,10):
    # select_append =

        # button_search = driver.find_element_by_xpath("/html/body/div[5]/header/div/div/div/div[2]/button[1]")
        # button_search.click()
        # # else:
        # # job_location.send_keys(search_job)
        #
# button functions. There should be a better way to write and implemenet these.        
def initApp():
    try: 
        Scraper.login(Scraper, username, password)   
    except:
        pass
def initJob():
    try: 
        Scraper.job_scrapes(Scraper)   
    except:
        pass

#Tkinter Interface with 2 buttons
root = Tk()
root.title("Linkedin Scraper")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Button(mainframe, text="Linkedin Login", command=initApp).grid(column=3, row=3, sticky=W)
ttk.Button(mainframe, text="Linkedin Job Scrape", command=initJob).grid(column=4, row=3, sticky=W)

# ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
# ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
# ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)


root.bind("<Return>", initApp)
root.bind("<Return>", initJob)

root.mainloop()
# 
# initApp()
# Scraper.initApp(Scraper)
# Scraper.login(Scraper, username, password)
# Scraper.job_scrapes(Scraper)


if __name__ == "__main__":
    pass

# print(main.text)


'''
junk code

'''

# def emberIter(self, selection):
# selector = input('Select 1-10:  ')
# if selector == (int > 0):
# if selector == i in range(1,10):
# selector = search_list(selector)
# return selector
# else:
# pass
# else:
# pass
#
