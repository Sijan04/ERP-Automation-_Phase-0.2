# #After going to leave we need to create Leave type

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
import time

# Setup Faker
fake = Faker()           #Fake data-generator-add

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

    # 2. Click Leave Type
    leave_type_link = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//a[@href="/hrm/leave-type" and .//div[contains(text(), "Leave Type")]]')
    ))
    leave_type_link.click()
    print("✅ Clicked Leave Type")

    # Click Add Leave Type button
    add_leave_type_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//button[contains(., "Add Leave Type")]')
    ))
    add_leave_type_button.click()
    print("✅ Clicked Add Leave Type button")

    # Generate fake leave type data
    fake_class_name = fake.job()  # e.g., 'Software Engineer'
    short_code = ''.join([word[0] for word in fake_class_name.split()]).upper()  # e.g., 'SE'

    # Fill in Leave Name
    leave_name_input = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//input[@placeholder="Enter Leave Name"]')
    ))
    leave_name_input.clear()
    leave_name_input.send_keys(fake_class_name)

    # Fill in Short Code
    short_code_input = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//input[@placeholder="Enter Short Code"]')
    ))
    short_code_input.clear()
    short_code_input.send_keys(short_code)

    print(f"✅ Entered Leave Name: {fake_class_name}")
    print(f"✅ Entered Short Code: {short_code}")

    time.sleep(2)

    # Find the label for "Maternity Leave"
    label = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//label[text()="Maternity Leave"]')
    ))

    # Get the value of the "for" attribute
    toggle_id = label.get_attribute("for")

    # Use the toggle ID to locate the input (toggle switch)
    toggle_input = driver.find_element(By.ID, toggle_id)

    # Click the toggle
    toggle_input.click()

    print("✅ Toggled Maternity Leave")

    time.sleep(1)

    # Find the label for "Unpaid Leave"
    label = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//label[text()="Unpaid Leave"]')
    ))

    # Get the value of the "for" attribute
    toggle_id = label.get_attribute("for")

    # Use the toggle ID to locate the input (toggle switch)
    toggle_input = driver.find_element(By.ID, toggle_id)

    # Click the toggle
    toggle_input.click()

    print("✅ Toggled Unpaid Leave")

    time.sleep(1)
    # Click the final "Add" submit button
    submit_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//button[normalize-space(text())="Add"]')
    ))
    submit_button.click()
    print("✅ Submitted the form")

except Exception as e:
    print("❌ Error:", e)

time.sleep(2)
driver.quit()
