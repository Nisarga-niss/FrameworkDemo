from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://practicetestautomation.com/practice-test-login/")
driver.find_element(By.ID,"username").send_keys("student")
driver.find_element(By.ID,"password").send_keys("Password1235")
driver.find_element(By.ID,"submit").click()

driver.quit()