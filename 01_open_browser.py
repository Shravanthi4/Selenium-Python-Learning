from selenium import webdriver

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.google.com")

print(driver.title)

input("Press Enter to close the browser...")

driver.quit()