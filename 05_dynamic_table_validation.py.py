from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Launch Chrome browser
driver = webdriver.Chrome()

# Maximize the browser window
driver.maximize_window()

# Open the practice website
driver.get("https://the-internet.herokuapp.com/")

# Click on "Sortable Data Tables"
driver.find_element(By.LINK_TEXT, "Sortable Data Tables").click()

# Find all rows in the first table
rows = driver.find_elements(By.XPATH, "//table[@id='table1']/tbody/tr")

# Print the total number of rows
print("Number of rows:", len(rows))

print("\nTable Data:\n")

# Print each row using a loop
for row in rows:
    print(row.text)

# Keep the browser open until the user presses Enter
input("\nPress Enter to close the browser...")

# Close the browser
driver.quit()