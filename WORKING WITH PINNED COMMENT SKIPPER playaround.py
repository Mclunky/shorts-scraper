
import time, os
import csv
import json
from itertools import zip_longest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# prompt user for the YouTube channel link
short_link = input("Enter the YouTube short link: ")

# create a new Chrome browser instance
driver = webdriver.Chrome(options=options)
driver.get(short_link)
driver.set_window_size(1920, 1080)# wait for the page to load

# Initialize an empty list
URL_list = []  
dupedURL_list = []  
title_list = []        
y=0 # Initialize the amount of times the loop has run
x=30 # Set the amount of times the loop should run
t=0
titleRough="Placeholder"
a=2
time.sleep(7) 

# iterate through the x amount of vids  
while y <= x:

    #start on second video
    driver.find_element(By.CSS_SELECTOR, "#navigation-button-down > ytd-button-renderer:nth-child(1) > yt-button-shape:nth-child(1) > button:nth-child(1)").click()
    time.sleep(6)


    astr="["+str(a)+"]"
    driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer"+astr+"/div[3]/ytd-reel-player-overlay-renderer/div[2]/div[4]/ytd-button-renderer/yt-button-shape/label/button").click()
    a=a+1
    
    time.sleep(2)
    
    try:
        pinCheck=driver.find_element(By.CSS_SELECTOR, "yt-formatted-string.ytd-pinned-comment-badge-renderer > span:nth-child(1)").is_displayed()
        if pinCheck == True:
            print("skip")
        
    #handle element not found
    except StaleElementReferenceException:
        print("No pinned comment")
        
        #save comment for new title
        try: 
            titleRough=driver.find_element(By.XPATH, '//*[@id="content-text"]').text
            #remove the /n from the title and replace with "  "
            titleRough=titleRough.replace("\n", "  ")

            # Split the string based on "Edit:"
            parts = titleRough.split("Edit:")

            # Take the first part of the split (everything before "Edit:")
            title = parts[0]

            print(title)

            #error handle for unable to locate 'title'

        except NoSuchElementException:
        # Handle the NoSuchElementException here
            print("Element not found. Performing alternative actions or error handling.")

        if titleRough == None:
            print("skip")
        #handle element not being found
        else:
            title_list.append(title)
            url = driver.current_url
            URL_list.append(url)
    
    except NoSuchElementException:
        print("No pinned comment")

        #save comment for new title
        try: 
            titleRough=driver.find_element(By.XPATH, '//*[@id="content-text"]').text
            #remove the /n from the title and replace with "  "
            titleRough=titleRough.replace("\n", "  ")

            # Split the string based on "Edit:"
            parts = titleRough.split("Edit:")

            # Take the first part of the split (everything before "Edit:")
            title = parts[0]

            print(title)

            #error handle for unable to locate 'title'
            if titleRough == None:
                print("skip")

            else:
                title_list.append(title)
                url = driver.current_url
                URL_list.append(url)

        except NoSuchElementException:
            # Handle the NoSuchElementException here
            print("Element not found. Performing alternative actions or error handling.")

        

    
    #skip if element is displayed
    

    #append lists
        

   
   
        y=y+1
        print(y)
        print(title_list)
        print(URL_list)

  

combineList=[(URL_list), (title_list)]
newCombList=zip(*combineList)        
print(newCombList)

def create_csv(filename, data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for item in data:
            writer.writerows([item])
    


    # Specify the filename for the CSV file
csv_filename ="C:/Users/Ohio/Documents/Shorts Scraper/my_file.csv"

def create_csv(filename, data):
    with open(filename, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        for item in data:
            writer.writerows([item])

# Specify the filename for the CSV file
csv_filename ="C:/Users/Ohio/Documents/Shorts Scraper/my_file.csv"

# Call the function to create the CSV file
create_csv(csv_filename, newCombList)
  
 
print(y)
print(newCombList)

driver.quit()
