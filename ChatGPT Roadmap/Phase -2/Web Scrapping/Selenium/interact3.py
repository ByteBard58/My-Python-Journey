from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Firefox()
driver.get("https://www.bing.com")
searchbar = driver.find_element(By.ID,"sb_form_q")
text = searchbar.send_keys("BUET")
searchbar.submit()
WebDriverWait(driver,5).until(
  ec.presence_of_element_located((By.PARTIAL_LINK_TEXT, "BUET"))
)
target = driver.find_element(By.PARTIAL_LINK_TEXT, "BUET")
target.click()

