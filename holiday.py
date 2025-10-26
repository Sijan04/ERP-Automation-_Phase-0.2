# Holiday

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

    # Wait and click the Leave dropdown
    leave_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//button[.//div[text()="Leave"]]')  # ✅ Correct target
    ))
    leave_button.click()
    print("✅ Clicked Leave dropdown")

    # Click-Holiday-Dropdown
    leave_type_link = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//a[@href="/hrm/holidays" and .//div[contains(text(), "Holiday")]]')
    ))
    leave_type_link.click()
    print("✅ Clicked Holiday")

    # Click Add holiday Type button
    add_leave_type_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//button[contains(., "Add Holiday")]')
    ))
    add_leave_type_button.click()
    print("✅ Clicked Add Leave Type button")

    # Fill Holiday Name with Faker
    holiday_name = fake.word().capitalize() + " Holiday"
    holiday_name_input = wait.until(EC.element_to_be_clickable(
    (By.NAME, "holidays.0.name")
    ))
    holiday_name_input.send_keys(holiday_name)
    print(f"✅ Holiday name entered: {holiday_name}")

    # Click From Date picker button
    from_date_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//button[contains(.,"Pick a date")][1]')
    ))
    from_date_button.click()
    print("✅ Opened From Date picker")

    # Select today's date in calendar (Mui Date Picker)
    today_date = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//button[contains(@class, "MuiPickersDay-root") and @tabindex="0"]')
    ))
    driver.execute_script("arguments[0].click();", today_date)
    print("✅ Selected today as From Date")









except Exception as e:
    print("❌ Error:", e)

time.sleep(3)
driver.quit()