# #After Login-go into the HRM Module after that create class and submit form and add to the list


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
import time

# Setup Faker
# fake = Faker()           #Fake data-generator-add
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

wait = WebDriverWait(driver, 10)

# ✅ Load LocalStorage session
try:
    with open("localstorage.json", "r") as f:
        session_data = json.load(f)

    for key, value in session_data.items():
        driver.execute_script(f"localStorage.setItem('{key}', '{value}');")

    print("🔐 Session loaded from LocalStorage")

    # ✅ Refresh to apply session (this was missing in your code)
    driver.refresh()
    time.sleep(0.5)

except Exception as e:
    print("⚠️ Session not found:", e)

try:
    # Click HRM card
    hrm_card = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//div[contains(@class, "bg-card")]//img[contains(@src, "hrm")]/ancestor::div[contains(@class, "rounded-lg")]')
    ))
    hrm_card.click()
    print("✅ Clicked HRM card")

    # ✅ Now click Attendance module inside HRM
    attendance_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//div[text()='Attendance']/parent::button")
    ))
    attendance_button.click()
    print("✅ Clicked Attendance module")

    # ✅ Click Shifts link
    shifts_link = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//a[@href="/hrm/shifts" and .//div[text()="Shifts"]]')  # matches the link with Shifts text
    ))
    shifts_link.click()
    print("✅ Clicked Shifts link")

    # ✅ Click Add Shift button
    add_shift_btn = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//button[.//text()[normalize-space()="Add Shift"]]')
    ))
    add_shift_btn.click()
    print("✅ Clicked Add Shift button")

    # Generate a fake shift name
    fake_shift_name = fake.job()  # or fake.word(), fake.bs(), etc.

    # Enter the shift name
    input_field = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//input[@placeholder="Enter Shift name"]')
    ))
    input_field.clear()
    input_field.send_keys(fake_shift_name)
    print(f"✅ Entered shift name: {fake_shift_name}")

    # Generate a fake time in HH:MM format (24-hour)
    fake_start_time = fake.time(pattern="%H:%M")

    # Enter the start time
    start_time_input = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//input[@name="start_time"]')
    ))
    start_time_input.clear()
    start_time_input.send_keys(fake_start_time)
    print(f"✅ Entered start time: {fake_start_time}")

    # Generate End time in HH:MM format (24-hour)
    fake_end_time = fake.time(pattern="%H:%M")

    # Enter the End time
    end_time_input = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//input[@name="end_time"]')
    ))
    end_time_input.clear()
    end_time_input.send_keys(fake_end_time)
    print(f"✅ Entered end time: {fake_end_time}")

    # Click dropdown first
    org_dropdown = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//button[.//span[contains(text(),"Select Organization")]]')
    ))
    org_dropdown.click()
    print("✅ Opened Organization dropdown")

    # Step 2: Wait for the option to be clickable
    xyz_option = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//div[normalize-space()="xyz"]')
    ))
    xyz_option.click()

    time.sleep(4)
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
