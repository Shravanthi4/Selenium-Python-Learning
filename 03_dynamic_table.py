from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/tables")

rows = driver.find_elements(By.XPATH, "//table[@id='table1']/tbody/tr")

print("Number of rows:", len(rows))

print("\nTable Data:\n")

for row in rows:
    print(row.text)

input("\nPress Enter to close the browser...")

driver.quit()