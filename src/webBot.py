'''
Created on May 16, 2021

@author: dacoolestnerd
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date
#from selenium.webdriver.support.ui import Select

#local variables
user = 'dacoolestnerd'
password = 'Bsece123?'
day = str(date.today().day+2) #book three days in advance
primetime = "7:00 AM"
time = primetime
teeQueue = True

#print(day)
#myxpath = '//*[@id="main"]/div[6]/div/div[1]/div[2]/div[2]/div[4]/div/div/div[2]'

#open browser
browser = webdriver.Chrome(executable_path='/Users/Brett/Developer/chromedriver')
browser.get("https://www.sangabrielcc.com/login")
wait = WebDriverWait(browser,10)

#login
browser.find_element(By.ID, "masterPageUC_MPCA166_ctl00_ctl01_txtUsername").click()
browser.find_element(By.ID, "masterPageUC_MPCA166_ctl00_ctl01_txtUsername").send_keys(user)
browser.find_element(By.ID, "masterPageUC_MPCA166_ctl00_ctl01_txtPassword").send_keys(password)
browser.find_element(By.ID, "masterPageUC_MPCA166_ctl00_ctl01_txtPassword").send_keys(Keys.ENTER)

#navigate to tee sheet
element = wait.until(EC.element_to_be_clickable((By.ID, "ulMenuItem_100340")))
element.click()
#browser.find_element(By.ID,"ulMenuItem_100340").click()
browser.find_element(By.LINK_TEXT,"Book Tee Time").click()
element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Tee Times")))
#browser.find_element(By.LINK_TEXT,"Tee Times").click()
element.click()
browser.find_element(By.PARTIAL_LINK_TEXT,"Make").click()
#browser.find_element(By.CSS_SELECTOR, "ul:nth-child(1) > .topnav_item:nth-child(1) li:nth-child(1) span").click()


#book earliest tee time available 
#xavailable = "/html/body/div[3]/div/div[3]/div[6]/div[4]/div[1]/div/div/table/tbody/tr[4]/td[@title='Tee Times Available']"
#element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT,day))#date is available
#                     & EC.text_to_be_present_in_element((By.XPATH,xavailable,"Tee Times Available")))#
element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT,day)))
element.click()
#browser.find_element(By.LINK_TEXT, day).click()
while teeQueue:
    elem = browser.find_elements_by_link_text(time)
    if len(elem)>0:
        elem[0].click()
        teeQueue = False
    else:
        print("Tee Sheet not available")
        element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT,day)))
        element.click()
        #teeQueue = False 

#set the player list
# 12 | click | css=li:nth-child(4) > div | 
browser.find_element(By.CSS_SELECTOR, "li:nth-child(4) > div").click() #main user
# 13 | click | xpath=//div[4]/div/div/div[2]/span | 
browser.find_element(By.XPATH, "//div[4]/div/div/div[2]/span").click() #TBD
browser.find_element(By.XPATH, "//div[4]/div/div/div[2]/span").click() #TBD

#set transportation method
browser.find_element(By.CSS_SELECTOR, "#slot_player_row_0 .transport_type").click()
dropdown = browser.find_element(By.CSS_SELECTOR, "#slot_player_row_0 .transport_type")
dropdown.find_element(By.XPATH, "//option[. = 'WLK']").click()

#submit tee time
browser.find_element(By.LINK_TEXT,"Submit Request").click()

#close browser
#browser.close()
