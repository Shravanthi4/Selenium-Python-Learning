from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/")

driver.find_element(By.LINK_TEXT, "Sortable Data Tables").click()

print(driver.title)

input("Press Enter to close the browser...")

driver.quit()