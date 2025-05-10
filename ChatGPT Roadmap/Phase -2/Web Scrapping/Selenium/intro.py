# Selenium is a python module used to automate web browsers
# We are gonna use firefox because chrome sucks

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import time

## Ways of opening the webdriver
## 1. Manual way
# service = Service(executable_path="usr/local/bin/geckodriver")
# driver = webdriver.Firefox(service=service)

## 2. Automatic detection (Recommended, works only if the selenium.exe file is in system PATH) 
# driver = webdriver.Firefox()          
# driver.get("https://apple.com")
# time.sleep(10)
# driver.quit()         ## Quits the browser after 10 secconds