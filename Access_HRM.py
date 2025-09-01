#After Login go into the HRM Module

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://amarsolution.xyz/login")
driver.maximize_window()

try:
    # Login
    driver.find_element(By.NAME, "email").send_keys("admin@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("password")
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    wait = WebDriverWait(driver, 15)

    # Wait for HRM card to load and click it
    hrm_card = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//div[contains(@class, "bg-card")]//img[contains(@src, "hrm")]/ancestor::div[contains(@class, "rounded-lg")]')
    ))
    hrm_card.click()
    print("Clicked HRM card")

    # Wait for the Employee button to appear and click it
    employee_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//button[.//div[text()="Employee"]]')
    ))
    employee_button.click()
    print("Clicked Employee dropdown")

    # Wait for the "Employee List" to be visible (submenu item)
    employee_list_item = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//a[contains(text(), "Employee List")]')
    ))
    employee_list_item.click()
    print("Clicked Employee List")

except Exception as e:
    print("Error:", e)

# Wait before closing (for demo/testing)
time.sleep(10)
driver.quit()