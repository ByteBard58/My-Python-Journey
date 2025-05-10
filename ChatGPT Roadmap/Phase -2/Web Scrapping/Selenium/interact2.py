from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()
driver.get("https://www.wikipedia.org/")
# WebDriverWait(driver,10).until(        ## Waits for 10 seccond (max) for the required element, if requirement isn't matched, the programm crashes
#   EC.presence_of_element_located(())
# )

target = driver.find_element(By.ID, "searchInput")
target.clear() 
target.send_keys("CIA"+Keys.ENTER)

time.sleep(13)
driver.quit()