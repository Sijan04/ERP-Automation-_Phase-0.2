# #After going to-leave we need to create-Leave Group


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
import time

# Setup Faker
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

    # 2. Click Group
    leave_group_link = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//a[@href="/hrm/leave-group" and .//div[contains(text(), "Leave Group")]]')
    ))
    leave_group_link.click()
    print("✅ Clicked Leave Group")


    #  Click Add Leave Group button
    add_leave_group_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//button[contains(., "Add Leave Group")]')
    ))
    add_leave_group_button.click()
    print("✅ Clicked Add Leave Group button")

    # --- Fill Leave Group Name ---
    leave_group_name = fake.company()
    name_input = wait.until(EC.presence_of_element_located((By.NAME, "name")))
    name_input.clear()
    name_input.send_keys(leave_group_name)
    print(f"✅ Entered Leave Group Name: {leave_group_name}")

    # 8. Click Leave type dropdown (new button with role="combobox")
    leave_type_dropdown = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//button[@role="combobox" and contains(text(), "Select an option")]')
    ))
    leave_type_dropdown.click()

    # Click the 'Medical Leave' option using data-value
    medical_leave_option = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//div[@role="option" and @data-value="medical leave"]')
    ))
    medical_leave_option.click()

    # Fill in leave_count using spinner arrows
    leave_count = fake.random_int(min=1, max=10)

    leave_count_input = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//input[@placeholder="Enter Leave Count"]')
    ))

    leave_count_input.click()
    leave_count_input.clear()
    leave_count_input.send_keys(str(leave_count))

    # --- Submit the form ---
    add_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//button[@type="submit" and text()="Add"]'))
    )
    add_button.click()
    print("✅ Form successfully submitted!")

    time.sleep(8)
except Exception as e:
    print("❌ Error:", e)

time.sleep(6)
driver.quit()













