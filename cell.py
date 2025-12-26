from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
import json
import time
import random as r
import sys
import urllib.request as dataharvest
import urllib.error
import gzip
from selenium.webdriver.common.action_chains import ActionChains

listofIndexes = sys.argv[1:]


def waitforOpenings(listofIndexes):
    with dataharvest.urlopen("https://classes.rutgers.edu/soc/api/openSections.json?year=2026&term=1&campus=NB") as data:
      try:
        jsondata = json.loads((gzip.decompress(data.read())).decode('utf-8'))
      except urllib.error.URLError as e:
        print(f"Error fetching the URL: {e.reason}")
      except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
 


    for x in listofIndexes:
        if x in jsondata:
            snipeCourse(x)
            listofIndexes.remove(x)


def snipeCourse(index):
    try:
        
        customOptions = ChromeOptions()
        customOptions.add_argument(r"--user-data-dir=C:\Users\sarmi\Downloads\User Data") #Replace with your own chrome data directory
        customOptions.add_argument(r"--profile-directory=Profile 7") #Replace with your own profile name
        customOptions.add_experimental_option("excludeSwitches", ["enable-automation"])
        customOptions.add_experimental_option("useAutomationExtension", False)
        customOptions.add_argument("--disable-blink-features=AutomationControlled")
        browser = webdriver.Chrome(options=customOptions)

        while True:
            try:   
                browser.get(r"https://sims.rutgers.edu/webreg/chooseSemester.htm?login=cas")
                break
            except Exception as e:
                print(repr(e))
        
            
        time.sleep(r.uniform(0.7,1.2)) #Let the page load
        semchoice = browser.current_url

        if semchoice != "https://sims.rutgers.edu/webreg/chooseSemester.htm?login=cas":
            loginButton = browser.find_element(By.XPATH, '//*[@id="fm1"]/input[4]')
            pressBefore = browser.find_element(By.XPATH, "//input[@id='password']")
            bubble = ActionChains(browser)
            bubble.click(loginButton)
            bubble.perform()
            time.sleep(r.uniform(0.4,0.7)) #Emulating Human Reaction Time
        
           
        #--------------------Choose Semester Page------------------------------------------------------------------
        if n:=browser.current_url != 'https://sims.rutgers.edu/webreg/chooseSemester.htm?login=cas':
            time.sleep(r.uniform(0.5,0.8)) #Let the page load
        time.sleep(r.uniform(0.3,0.5))
        #From top to bottom of the semester choice choose a semester with its corresponding id semesterSelection1, semesterSelection2, semesterSelection3, semesterSelection4
        semesterChoice =  browser.find_element(By.ID, 'semesterSelection4')
        submitSemesterChoice = browser.find_element(By.XPATH, '//*[@id="submit"]')
     
        time.sleep(r.uniform(0.4,0.7)) #Emulating Human Reaction Time
        semesterChoice.click()
        time.sleep(r.uniform(0.4,0.7)) #Emulating Human Reaction Time
        submitSemesterChoice.click()

        #--------------------Enter Index Page------------------------------------------------------------------
        time.sleep(r.uniform(0.7,1.2)) #Let the page load
        enterIndex = browser.find_element(By.ID, "i1")
        submit = browser.find_element(By.ID, "submit")
        enterIndex.send_keys(index)
        time.sleep(r.uniform(0.4,0.7)) #Emulating Human Reaction Time
        submit.click()
        time.sleep(1) #Wait
        #browser.quit() #End browser

    except Exception as e:
        print(repr(e))
        print("please restart script")

if __name__ == "__main__":
   while True:
       waitforOpenings(listofIndexes)

       if len(listofIndexes) == 0:
          print("Snipe complete")
          sys.exit()
      
       time.sleep(30.02)




    

