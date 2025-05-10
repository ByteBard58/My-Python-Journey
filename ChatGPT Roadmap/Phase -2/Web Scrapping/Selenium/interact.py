from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Going to wikipedia website and searching BUET
driver = webdriver.Firefox()
driver.get("https://en.wikipedia.org")
navigate = driver.find_element(By.CLASS_NAME, "cdx-text-input__input")
navigate.send_keys("BUET" + Keys.ENTER)
time.sleep(5)
driver.quit()
