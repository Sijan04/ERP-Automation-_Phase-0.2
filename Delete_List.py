from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# # Setup WebDriver
# driver = webdriver.Chrome()
# driver.get("https://amarsolution.xyz/login")
# driver.maximize_window()
# wait = WebDriverWait(driver, 15)
#
# try:
#     # --- Login ---
#     driver.find_element(By.NAME, "email").send_keys("admin@gmail.com")
#     driver.find_element(By.NAME, "password").send_keys("password")
#     driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
#     print("✅ Logged in")
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
    # --- Click HRM card ---
    hrm_card = wait.until(EC.element_to_be_clickable((
        By.XPATH,
        '//div[contains(@class, "bg-card")]//img[contains(@src, "hrm")]/ancestor::div[contains(@class, "rounded-lg")]'
    )))
    hrm_card.click()
    print("✅ Clicked HRM card")

    # --- Click Employee dropdown ---
    employee_button = wait.until(EC.element_to_be_clickable((
        By.XPATH, '//button[.//div[text()="Employee"]]'
    )))
    employee_button.click()
    print("✅ Clicked Employee dropdown")

    # --- Click Employee Classes ---
    employee_classes_link = wait.until(EC.element_to_be_clickable((
        By.XPATH, '//a[@href="/hrm/employee-classes" and .//div[contains(text(), "Employee Classes")]]'
    )))
    employee_classes_link.click()
    print("✅ Clicked Employee Classes")

    # --- Click "Add Employee Class" ---
    add_class_button = wait.until(EC.element_to_be_clickable((
        By.XPATH, '//button[contains(., "Add Employee Class")]'
    )))
    add_class_button.click()
    print("✅ Clicked 'Add Employee Class'")

    # --- Enter class name ---
    class_name = "LeoDeleteTest33345"
    input_field = wait.until(EC.visibility_of_element_located((
        By.XPATH, '//input[@placeholder="Enter employee class name"]'
    )))
    input_field.clear()
    input_field.send_keys(class_name)
    print(f"✅ Entered class name: {class_name}")

    # --- Submit form ---
    submit_button = wait.until(EC.element_to_be_clickable((
        By.XPATH, '//button[normalize-space(text())="Add"]'
    )))
    submit_button.click()
    print("✅ Submitted class form")

    # --- Wait for row to appear ---
    row_xpath = f'//tr[.//td[contains(text(), "{class_name}")]]'
    wait.until(EC.presence_of_element_located((By.XPATH, row_xpath)))
    print("✅ New class row appeared")

    # --- Re-fetch the row (in case DOM reloaded) ---
    row = driver.find_element(By.XPATH, row_xpath)

    # --- Click delete button ---
    delete_button = row.find_element(By.XPATH, './/button[.//svg[contains(@class, "lucide-trash2")]]')
    driver.execute_script("arguments[0].scrollIntoView(true);", delete_button)
    driver.execute_script("arguments[0].click();", delete_button)
    print("✅ Clicked delete button")

    # --- Allow small time for modal animation ---
    time.sleep(1)

    # --- Wait for and click confirm button in modal ---
    confirm_button = wait.until(EC.element_to_be_clickable((
        By.XPATH, '//div[@role="dialog" and @data-state="open"]//button[normalize-space(text())="Confirm"]'
    )))
    confirm_button.click()
    print("✅ Confirmed deletion")

    # --- Verify row is removed ---
    wait.until_not(EC.presence_of_element_located((By.XPATH, row_xpath)))
    print("✅ Row successfully deleted")

except Exception as e:
    print("❌ Error occurred:", e)

finally:
    time.sleep(2)
    driver.quit()
    print("✅ Browser closed")
