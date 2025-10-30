# Holiday

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


    # Click the date picker button to open the calendar #Calander Select Code From Date

    date_picker_opener = wait.until(EC.element_to_be_clickable((
        By.XPATH, '//button[contains(@aria-haspopup,"dialog")]'
    )))
    date_picker_opener.click()

    # Click #the-day 26

    target_day = "26"
    day_button = wait.until(EC.element_to_be_clickable((
        By.XPATH, f'//button[@name="day" and normalize-space()="{target_day}"]'
    )))
    day_button.click()

    # Click the To Date picker button to open the calendar
    to_date_picker = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '(//button[contains(@aria-haspopup,"dialog")])[2]')
    ))
    to_date_picker.click()

    # Select the-day 26 again or any target day
    day_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, f'//button[@name="day" and normalize-space()="{target_day}"]')
    ))
    day_button.click()
    print(f"✅ Selected To Date: {target_day}")

    # Generate fake note text
    note_text = fake.sentence(nb_words=6)

    # Enter the holiday note
    note_field = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//input[@name="holidays.0.note" and @placeholder="Enter note"]')
    ))
    note_field.clear()
    note_field.send_keys(note_text)
    print(f"✅ Entered note: {note_text}")



    # Click Save/Submit button
    submit_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//button[normalize-space(text())="Save"]')
    ))
    submit_button.click()
    print("✅ Submitted Designation form")


except Exception as e:
    print("❌ Error:", e)

time.sleep(3)
driver.quit()