#
#
#
#
# import json, time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from faker import Faker
#
# fake = Faker()
#
# driver = webdriver.Chrome()
# driver.get("https://amarsolution.xyz/")
# driver.maximize_window()
#
# wait = WebDriverWait(driver, 10)
#
# # ✅ Load LocalStorage session
# try:
#     with open("localstorage.json", "r") as f:
#         session_data = json.load(f)
#
#     for key, value in session_data.items():
#         driver.execute_script("localStorage.setItem(arguments[0], arguments[1]);", key, value)
#
#     print("🔐 Session loaded from LocalStorage")
#     driver.refresh()
#     time.sleep(1)
#
# except Exception as e:
#     print("⚠️ Session not found:", e)
#
# try:
#     # ✅ Click HRM card
#     hrm_card = wait.until(EC.visibility_of_element_located((
#         By.XPATH, '//div[contains(@class, "bg-card")]//img[contains(@src, "hrm")]/ancestor::div[contains(@class, "rounded-lg")]'
#     )))
#     hrm_card.click()
#     print("✅ Clicked HRM card")
#
#     # ✅ Click Attendance module inside HRM
#     attendance_button = wait.until(EC.element_to_be_clickable((
#         By.XPATH, "//div[text()='Attendance']/parent::button"
#     )))
#     attendance_button.click()
#     print("✅ Clicked Attendance module")
#
#     # ✅ Click Attendances List link
#     attendances_list_link = wait.until(EC.element_to_be_clickable((
#         By.XPATH, "//a[@href='/hrm/attendances-list']"
#     )))
#     attendances_list_link.click()
#     print("✅ Clicked 'Attendances List' link")
#
#     # ✅ Click Add Attendance button
#     add_attendance_button = wait.until(EC.element_to_be_clickable((
#         By.XPATH, "//button[contains(., 'Add Attendance')]"
#     )))
#     add_attendance_button.click()
#     print("✅ Clicked 'Add Attendance' button")
#
#     # ✅ Wait for Search Input to appear
#     search_input = wait.until(EC.element_to_be_clickable((
#         By.XPATH, "//input[@placeholder='Search and select options']"
#     )))
#     search_input.click()
#     print("✅ Clicked search input")
#
#     # ✅ Click search box
#     search_input = wait.until(EC.element_to_be_clickable((
#         By.XPATH, "//input[@placeholder='Search and select options']"
#     )))
#     search_input.click()
#     search_input.clear()
#     search_input.send_keys("Sabbir Alam")
#     print("✅ Typed 'Sabbir Alam'")
#
#     # ✅ Wait for dropdown option with that name and click it
#     sabbir_option = wait.until(EC.element_to_be_clickable((
#         By.XPATH, "//div[contains(text(), 'Sabbir Alam')]"
#     )))
#     sabbir_option.click()
#     print("✅ Selected employee: Sabbir Alam")
#
# except Exception as e:
#     print("❌ Error:", e)
#
# time.sleep(2)
# driver.quit()




import json, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from selenium.webdriver.common.keys import Keys

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
        driver.execute_script("localStorage.setItem(arguments[0], arguments[1]);", key, value)
    print("🔐 Session loaded from LocalStorage")
    driver.refresh()
    time.sleep(1)
except Exception as e:
    print("⚠️ Session not found:", e)

try:
    # ✅ Click HRM card
    hrm_card = wait.until(EC.visibility_of_element_located((By.XPATH,
        '//div[contains(@class, "bg-card")]//img[contains(@src, "hrm")]/ancestor::div[contains(@class, "rounded-lg")]'
    )))
    hrm_card.click()
    print("✅ Clicked HRM card")

    # ✅ Click Attendance module
    attendance_button = wait.until(EC.element_to_be_clickable((By.XPATH,
        "//div[text()='Attendance']/parent::button"
    )))
    attendance_button.click()
    print("✅ Clicked Attendance module")

    # ✅ Click Attendances List
    attendances_list_link = wait.until(EC.element_to_be_clickable((By.XPATH,
        "//a[@href='/hrm/attendances-list']"
    )))
    attendances_list_link.click()
    print("✅ Clicked 'Attendances List' link")

    # ✅ Click Add Attendance
    add_attendance_button = wait.until(EC.element_to_be_clickable((By.XPATH,
        "//button[contains(., 'Add Attendance')]"
    )))
    add_attendance_button.click()
    print("✅ Clicked 'Add Attendance' button")

    # ✅ Type in employee search box
    search_input = wait.until(EC.element_to_be_clickable((By.XPATH,
        "//input[@placeholder='Search and select options']"
    )))
    search_input.click()
    search_input.clear()
    search_input.send_keys("Sabbir Alam")
    print("✅ Typed 'Sabbir Alam'")

    # ✅ Wait for dropdown list to load fully

    time.sleep(1.5)

    # ✅ Try clicking the Sabbir Alam option with JS (more reliable)
    sabbir_option = wait.until(EC.presence_of_element_located((By.XPATH,
        "//div[contains(text(), 'Sabbir Alam')]"
    )))
    driver.execute_script("arguments[0].click();", sabbir_option)
    print("✅ Selected employee: Sabbir Alam")


#not complete-------------------------------------------






except Exception as e:
    print("❌ Error:", e)

time.sleep(2)
driver.quit()



