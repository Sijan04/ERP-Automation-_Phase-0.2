#
#
#
# # Employee_Grade_Form_Create
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from faker import Faker
# import time
# import random
#
# # Setup Faker
# fake = Faker()
#
# driver = webdriver.Chrome()
# driver.get("https://amarsolution.xyz/login")
# driver.maximize_window()
#
# try:
#     # Login
#     driver.find_element(By.NAME, "email").send_keys("admin@gmail.com")
#     driver.find_element(By.NAME, "password").send_keys("password")
#     driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
#
#     wait = WebDriverWait(driver, 15)
#
#     # Click HRM card
#     hrm_card = wait.until(EC.visibility_of_element_located(
#         (By.XPATH, '//div[contains(@class, "bg-card")]//img[contains(@src, "hrm")]/ancestor::div[contains(@class, "rounded-lg")]')
#     ))
#     hrm_card.click()
#     print("✅ Clicked HRM card")
#
#     # Click Employee dropdown
#     employee_button = wait.until(EC.element_to_be_clickable(
#         (By.XPATH, '//button[.//div[text()="Employee"]]')
#     ))
#     employee_button.click()
#     print("✅ Clicked Employee dropdown")
#
#     # Click Departments
#     departments_link = wait.until(EC.element_to_be_clickable(
#         (By.XPATH, '//a[@href="/hrm/departments" and .//div[text()="Departments"]]')
#     ))
#     departments_link.click()
#     print("✅ Clicked Departments")
#
#     # Click "Add Department" button
#     add_department_button = wait.until(EC.element_to_be_clickable(
#         (By.XPATH, '//button[contains(., "Add Department")]')
#     ))
#     add_department_button.click()
#     print("✅ Clicked Add Department button")
#
#     # Generate fake department name
#     department_name = fake.company()
#
#     # Enter the department name
#     name_field = wait.until(EC.visibility_of_element_located(
#         (By.XPATH, '//input[@name="name" and @placeholder="Enter department name"]')
#     ))
#     name_field.clear()
#     name_field.send_keys(department_name)
#     print(f"✅ Entered department name: {department_name}")
#
#     time.sleep(1)
#
#     # Click Save/Submit button
#     submit_button = wait.until(EC.element_to_be_clickable(
#         (By.XPATH, '//button[normalize-space(text())="Add"]')
#     ))
#     submit_button.click()
#     print("✅ Submitted Department form")
#
#
# except Exception as e:
#     print("❌ Error:", e)
#
# time.sleep(3)
# driver.quit()






# Employee_Grade_Form_Create_With_Session.py

import json, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
fake = Faker()

driver = webdriver.Chrome()
driver.get("https://amarsolution.xyz/")
driver.maximize_window()

wait = WebDriverWait(driver, 20)

# ✅ Load LocalStorage saved session
try:
    with open("localstorage.json", "r") as f:
        session_data = json.load(f)

    for key, value in session_data.items():
        driver.execute_script(f"localStorage.setItem('{key}', '{value}');")

    print("🔐 Session loaded successfully!")

except Exception as e:
    print("⚠️ Session not found, please login first:", e)
    driver.quit()
    exit()

# ✅ Refresh to apply session
driver.refresh()

# ✅ Wait until Dashboard loads
try:
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//div[contains(text(), "HRM")]')
    ))
    print("✅ Dashboard Loaded via Session ✅")
except:
    print("⚠️ Session Expired! Login required again.")
    driver.quit()
    exit()

try:
    # ✅ Click HRM card
    hrm_card = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//div[contains(@class, "bg-card")]//img[contains(@src, "hrm")]/ancestor::div[contains(@class, "rounded-lg")]')
    ))
    hrm_card.click()
    print("✅ Clicked HRM card")

    # ✅ Click Employee dropdown
    employee_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//button[.//div[text()="Employee"]]')
    ))
    employee_button.click()
    print("✅ Clicked Employee dropdown")

    # ✅ Click Departments
    departments_link = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//a[@href="/hrm/departments" and .//div[text()="Departments"]]')
    ))
    departments_link.click()
    print("✅ Clicked Departments")

    # ✅ Click "Add Department" button
    add_department_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//button[contains(., "Add Department")]')
    ))
    add_department_button.click()
    print("✅ Clicked Add Department button")

    # ✅ Enter department name using Fake data
    department_name = fake.company()

    name_field = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//input[@name="name" and @placeholder="Enter department name"]')
    ))
    name_field.clear()
    name_field.send_keys(department_name)
    print(f"✅ Entered department name: {department_name}")

    time.sleep(1)

    # ✅ Click Add button
    submit_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//button[normalize-space(text())="Add"]')
    ))
    submit_button.click()
    print("✅ Submitted Department Form ✅")

except Exception as e:
    print("❌ Error:", e)

time.sleep(3)
driver.quit()
