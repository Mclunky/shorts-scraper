import time, os
import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#######accomodate for missing files error handling

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# create a new Chrome browser instance
driver = webdriver.Chrome(options=options)
driver.set_window_size(1920, 1080)# wait for the page to load


count = 0
dir_path = '/home/ohio/video'

for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, path)):
        count += 1
print("   ", count, " Videos found in the videos folder, ready to upload...")
time.sleep(6)

driver.get("https://studio.youtube.com")

    #driver.execute_script("window.open('{}', '_blank')".format("https://studio.youtube.com"))
    #driver.switch_to.window(driver.window_handles[i+1])
    # Login
email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'identifierId')))
email.send_keys("hgfd9691@gmail.com")
email.send_keys(Keys.RETURN)

time.sleep(5)

password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'Passwd')))
password.send_keys("13qeadzc")
password.send_keys(Keys.RETURN)
time.sleep(56)
upload_button = driver.find_element(By.XPATH, '//*[@id="upload-icon"]')
upload_button.click()
time.sleep(5)

for i in range(count):
    


    dataset = "/home/ohio/Downloads/YTdownloader/my_file.csv"
    path = "/home/ohio/Videos"


    def download_dataset(dataset, path, i, end=0):
        dir_list = os.listdir(path)
        rows = []

        
        with open(dataset, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                rows.append(row)

        if end==0:
            end = len(rows)

        row = rows[i]
        url = row[0]
        filename = row[1]
        return filename

    newTitle=download_dataset(dataset, path, i, 10)

    file_input = driver.find_element(By.XPATH, '//*[@id="content"]/input')
    simp_path = 'video/'+newTitle+'.mp4'.format(str(i+1))
    abs_path = os.path.abspath(simp_path)
    
    if os.path.exists(abs_path):
    # The file exists, proceed with your script
        file_input.send_keys(abs_path)
    
    
        time.sleep(7)

        next_button = driver.find_element(By.XPATH, '//*[@id="next-button"]')
   
        notForKids = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'VIDEO_MADE_FOR_KIDS_NOT_MFK')))
        notForKids.click()
        time.sleep(5)

        for i in range(3):
            next_button.click()
            time.sleep(10)
  

        PublicButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="privacy-radios"]/tp-yt-paper-radio-button[3]')))
        PublicButton.click()
    
        done_button = driver.find_element(By.XPATH, '//*[@id="done-button"]/div')
        done_button.click()
        time.sleep(15)

    #close_button = driver.find_element(By.CSS_SELECTOR, 'close-button > div')

        close_button = driver.find_element(By.XPATH, '//*[@id="close-button"]/div')
        close_button.click()


    #If the close button errors, try swapping between XPATH and CSS selector
    #FULL XPATH  /html/body/ytcp-video-share-dialog/ytcp-dialog/tp-yt-paper-dialog/div[3]/ytcp-button/div
    #XPATH //*[@id="close-button"]/div
    #css selector    ytcp-button.ytcp-video-share-dialog > div:nth-child(2)
    #css selector    close-button > div
    
        create_button = driver.find_element(By.XPATH, '/html/body/ytcp-app/ytcp-entity-page/div/ytcp-header/header/div/ytcp-button/div')
        create_button.click()

        #upload_button = driver.find_element(By.XPATH, '/html/body/ytcp-app/ytcp-entity-page/div/ytcp-header/header/div/ytcp-text-menu/tp-yt-paper-dialog/tp-yt-paper-listbox/tp-yt-paper-item[1]/ytcp-ve/tp-yt-paper-item-body/div/div/div/yt-formatted-string')
        upload_button.click()
    else:
        print(f"File '{abs_path}' does not exist.")

driver.quit()