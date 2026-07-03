from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

driver.find_element(By.XPATH, "//button[text()='Start']").click()

wait = WebDriverWait(driver, 10)

hello = wait.until(
    EC.visibility_of_element_located((By.ID, "finish"))
)

print("Message:", hello.text)

input("Press Enter to close the browser...")

driver.quit()