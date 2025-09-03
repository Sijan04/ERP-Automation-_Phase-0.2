


# Designation

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
import time
import random

# Setup Faker
fake = Faker()

driver = webdriver.Chrome()
driver.get("https://amarsolution.xyz/login")
driver.maximize_window()

try:
    # Login
    driver.find_element(By.NAME, "email").send_keys("admin@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("password")
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    wait = WebDriverWait(driver, 15)

    # Click HRM card
    hrm_card = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//div[contains(@class, "bg-card")]//img[contains(@src, "hrm")]/ancestor::div[contains(@class, "rounded-lg")]')
    ))
    hrm_card.click()
    print("✅ Clicked HRM card")

    # Click Employee dropdown
    employee_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//button[.//div[text()="Employee"]]')
    ))
    employee_button.click()
    print("✅ Clicked Employee dropdown")

    # Click Section
    Sections_link = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//div[text()="Sections"]/ancestor::a')
    ))
    Sections_link.click()
    print("✅ Clicked Sections")

    # Click "Add section button"
    add_section_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//button[contains(., "Add Section")]')
    ))
    add_section_button.click()
    print("✅ Clicked Add Section button")

    # Generate fake section name
    section_name = fake.company()

    # Enter the section name
    name_field = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//input[@name="name" and @placeholder="Enter section name"]')
    ))
    name_field.clear()
    name_field.send_keys(section_name)
    print(f"✅ Entered department name: {section_name}")

    time.sleep(1)

    # Click Save/Submit button
    submit_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//button[normalize-space(text())="Add"]')
    ))
    submit_button.click()
    print("✅ Submitted Designation form")


except Exception as e:
    print("❌ Error:", e)

time.sleep(5)
driver.quit()