

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from faker import Faker
# import time
#
# # Setup Faker
# fake = Faker()          ##Fake data generator
#
# # Generate fake employee data
# first_name = fake.first_name()
# last_name = fake.last_name()
# email = fake.email()
# phone = fake.msisdn()[:11]  # 11-digit phone
# corporate_phone = fake.msisdn()[:11]
# joining_date = "2025/08/05"  # You can randomize if needed
#
# # Setup WebDriver
# driver = webdriver.Chrome()
# driver.get("https://amarsolution.xyz/login")
# driver.maximize_window()
#
# try:
#     wait = WebDriverWait(driver, 15)
#
#     # --- Login ---
#     driver.find_element(By.NAME, "email").send_keys("admin@gmail.com")
#     driver.find_element(By.NAME, "password").send_keys("password")
#     driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
#
#     # --- Click HRM card ---
#     hrm_card = wait.until(EC.element_to_be_clickable((By.XPATH,
#         '//div[contains(@class, "bg-card")]//img[contains(@src, "hrm")]/ancestor::div[contains(@class, "rounded-lg")]'
#     )))
#     hrm_card.click()
#
#     # --- Click Employee dropdown ---
#     employee_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[.//div[text()="Employee"]]')))
#     employee_button.click()
#
#     # --- Click Employee List ---
#     employee_list_item = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[.//div[contains(text(), "Employee List")]]')))
#     employee_list_item.click()
#
#     # --- Click "Add Employee" button ---
#     add_employee_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[normalize-space()="Add Employee"]')))
#     add_employee_button.click()
#
#     # --- Wait for Add Employee form ---
#     wait.until(EC.presence_of_element_located((By.NAME, "first_name")))
#
#     # --- Fill Employee Form ---
#     driver.find_element(By.NAME, "employee_unique_id").clear()
#     driver.find_element(By.NAME, "employee_unique_id").send_keys(email)
#     # Using email as Employee ID
#     driver.find_element(By.NAME, "first_name").send_keys(first_name)
#     driver.find_element(By.NAME, "last_name").send_keys(last_name)
#     driver.find_element(By.NAME, "phone").send_keys(phone)
#     driver.find_element(By.NAME, "corporate_phone").send_keys(corporate_phone)
#     # Email
#     driver.find_element(By.NAME, "email").send_keys(email)
#
#     # Click the date picker button to open the calendar #Calander Select Code.....
#     date_picker_opener = wait.until(EC.element_to_be_clickable((
#         By.XPATH, '//button[contains(@aria-haspopup,"dialog")]'
#     )))
#     date_picker_opener.click()
#
#     # Click the day (12th)
#     target_day = "12"
#     day_button = wait.until(EC.element_to_be_clickable((
#         By.XPATH, f'//button[@name="day" and normalize-space()="{target_day}"]'
#     )))
#     day_button.click()
#
#     # EXTRA STEP: Click outside the calendar to close it and submit the date
#     # Example: click on the label "Status" to blur the date picker
#     outside_click = wait.until(EC.element_to_be_clickable((
#         By.XPATH, '//label[contains(text(),"Status")]'
#     )))
#     #outside_click.click()
#     # Wait until the password field is clickable
#     password_field = wait.until(EC.element_to_be_clickable((By.NAME, "password")))
#
#     # Clear the field first (important for React-controlled inputs)
#     password_field.clear()
#
#     # Send the new password
#     password_field.send_keys("password@@Az12")
#     # Dropdown selections (example - adjust to your site)
#
#     # Wait until the toggle is clickable
#     toggle = wait.until(EC.element_to_be_clickable((By.ID, "status-toggle")))
#
#     # Check the current state
#     state = toggle.get_attribute("aria-checked")
#
#     # Click only if it's not already ON
#     if state != "true":
#         toggle.click()
#         print("✅ Toggle switched ON")
#     else:
#         print("ℹ️ Toggle already ON")
#     #driver.find_element(By.NAME, "location").send_keys("Dhaka")
#     # --- Select Location ---
#     # 1. Click the Location dropdown button
#     # --- Select Location: Dhaka ---
#     # 1. Click the Location dropdown
#     location_dropdown = wait.until(EC.element_to_be_clickable(
#         (By.XPATH, '//button[contains(.,"Location")]')
#     ))
#     location_dropdown.click()
#
#     # 2. Wait for the "Dhaka" option and click it
#     dhaka_option = wait.until(EC.element_to_be_clickable(
#         (By.XPATH, '//div[normalize-space()="Dhaka"]')
#     ))
#     dhaka_option.click()            #Last_Update
#
#     # 3. Click Organization dropdown
#     organization_dropdown = wait.until(EC.element_to_be_clickable(
#         (By.XPATH, '//button[contains(.,"Organization")]')
#     ))
#     organization_dropdown.click()
#
#     xyz_option = wait.until(EC.element_to_be_clickable(
#         (By.XPATH, '//div[normalize-space()="xyz"]')
#     ))
#     xyz_option.click()
#
#
#     # 4. Click Workplace dropdown
#     Work_Place_dropdown = wait.until(EC.element_to_be_clickable(
#         (By.XPATH, '//button[contains(.,"Work Place")]')
#     ))
#     Work_Place_dropdown.click()
#
#     remote_option = wait.until(EC.element_to_be_clickable(
#         (By.XPATH, '//div[normalize-space()="Remote"]')
#     ))
#     remote_option.click()
#
#
#     # 5. Click Department dropdown
#     Department_dropdown = wait.until(EC.element_to_be_clickable(
#         (By.XPATH, '//button[contains(.,"Department")]')
#     ))
#     Department_dropdown.click()
#
#     scm_option = wait.until(EC.element_to_be_clickable(
#         (By.XPATH, '//div[normalize-space()="SCM"]')
#     ))
#     scm_option.click()
#
#
#     # 6. Click Designation dropdown
#     Designation_dropdown = wait.until(EC.element_to_be_clickable(
#         (By.XPATH, '//button[contains(.,"Designation")]')
#     ))
#     Designation_dropdown.click()
#
#     it_officer_option = wait.until(EC.element_to_be_clickable(
#         (By.XPATH, '//div[normalize-space()="IT Officer"]')
#     ))
#     it_officer_option.click()
#
#
#
#     # 7. Click Section dropdown
#     Section_dropdown = wait.until(EC.element_to_be_clickable(
#         (By.XPATH, '//button[contains(.,"Section")]')
#     ))
#     Section_dropdown.click()
#
#     cold_storage_option = wait.until(EC.element_to_be_clickable(
#         (By.XPATH, '//div[normalize-space()="Cold Storage"]')
#     ))
#     cold_storage_option.click()
#     # 8. Click Shift dropdown
#     Shift_dropdown = wait.until(EC.element_to_be_clickable(
#         (By.XPATH, '//button[contains(.,"Shift")]')
#     ))
#     Shift_dropdown.click()
#
#     Shift_option = wait.until(EC.element_to_be_clickable(
#         (By.XPATH, '//div[normalize-space()="Full Time"]')
#     ))
#     Shift_option.click()
#
#     # 8. Click Employee Class dropdown
#     Employee_Class_dropdown = wait.until(EC.element_to_be_clickable(
#         (By.XPATH, '//button[contains(.,"Employee Class")]')
#     ))
#     Employee_Class_dropdown.click()
#
#     Employee_Class_option = wait.until(EC.element_to_be_clickable(
#         (By.XPATH, '//div[normalize-space()="Contractual"]')
#     ))
#     Employee_Class_option.click()
#
#
#     # 8. Click Employee Grade dropdown
#     Employee_Grade_dropdown = wait.until(EC.element_to_be_clickable(
#         (By.XPATH, '//button[contains(.,"Employee Grade")]')
#     ))
#     Employee_Grade_dropdown.click()
#
#     Employee_Grade_option = wait.until(EC.element_to_be_clickable(
#         (By.XPATH, '//div[normalize-space()="Grade 2"]')
#     ))
#     Employee_Grade_option.click()
#
#
#     # 8. Click Employment Status dropdown
#     Employee_Status_dropdown = wait.until(EC.element_to_be_clickable(
#         (By.XPATH, '//button[contains(.,"Employment Status")]')
#     ))
#     Employee_Status_dropdown.click()
#
#     Employee_Status_option = wait.until(EC.element_to_be_clickable(
#         (By.XPATH, '//div[normalize-space()="Full Time"]')
#     ))
#     Employee_Status_option.click()
#
#
#     # 8. Click Blood Group dropdown
#     Blood_Group_dropdown = wait.until(EC.element_to_be_clickable(
#         (By.XPATH, '//button[contains(.,"Blood Group")]')
#     ))
#     Blood_Group_dropdown.click()
#
#     Blood_Group_option = wait.until(EC.element_to_be_clickable(
#         (By.XPATH, '//div[normalize-space()="A+"]')
#     ))
#     Blood_Group_option.click()
#
#
#
#     # 8. Click Religion dropdown
#     Religion_dropdown = wait.until(EC.element_to_be_clickable(
#         (By.XPATH, '//button[contains(.,"Religion")]')
#     ))
#     Religion_dropdown.click()
#
#     Religion_option = wait.until(EC.element_to_be_clickable(
#         (By.XPATH, '//div[normalize-space()="Islam"]')
#     ))
#     Religion_option.click()
#
#     # 8. Click Gender dropdown
#     Gender_dropdown = wait.until(EC.element_to_be_clickable(
#         (By.XPATH, '//button[contains(.,"Gender")]')
#     ))
#     Gender_dropdown.click()
#
#     Gender_option = wait.until(EC.element_to_be_clickable(
#         (By.XPATH, '//div[normalize-space()="Male"]')
#     ))
#     Gender_option.click()
#
#
#     # 8. Click Role dropdown
#     Role_dropdown = wait.until(EC.element_to_be_clickable(
#         (By.XPATH, '//button[contains(.,"Role")]')
#     ))
#     Role_dropdown.click()
#
#     Role_option = wait.until(EC.element_to_be_clickable(
#         (By.XPATH, '//div[normalize-space()="Staff"]')
#     ))
#     Role_option.click()
#
#     # 8. Click Leave grp dropdown
#     Leave_Group_dropdown = wait.until(EC.element_to_be_clickable(
#         (By.XPATH, '//button[contains(.,"Leave Group")]')
#     ))
#     Leave_Group_dropdown.click()
#
#     Leave_Group_option = wait.until(EC.element_to_be_clickable(
#         (By.XPATH, '//div[normalize-space()="Leave Group 1"]')
#     ))
#     Leave_Group_option.click()
#
#     driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
#
#     # print(f"✅ Added fake employee: {first_name} {last_name}, {email}")
#     #
#     # # --- Submit the form ---
#     # driver.find_element(By.XPATH, '//button[normalize-space()="Update"]').click(
#     # )
#
# except Exception as e:
#     print("❌ Error:", e)
#
# finally:
#     time.sleep(4)
#     driver.quit()
#     print("✅ Browser closed")







# Employee_Create_AutoSession.py

import json, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
fake = Faker()

# Generate fake employee data
first_name = fake.first_name()
last_name = fake.last_name()
email = fake.email()
phone = fake.msisdn()[:11]
corporate_phone = fake.msisdn()[:11]

driver = webdriver.Chrome()
driver.get("https://amarsolution.xyz/")
driver.maximize_window()

wait = WebDriverWait(driver, 20)

# ✅ Load LocalStorage session
try:
    with open("localstorage.json", "r") as f:
        session_data = json.load(f)
    for key, value in session_data.items():
        driver.execute_script(f"localStorage.setItem('{key}', '{value}');")
    print("🔐 Session Loaded Successfully!")
except:
    print("⚠️ No session found! Run login_and_save_session.py first.")
    driver.quit()
    exit()

# ✅ Refresh to apply session
driver.refresh()

# ✅ Verify Dashboard visible -> session worked
try:
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//div[contains(text(), "HRM")]')
    ))
    print("✅ Logged in with Session ✅")
except:
    print("⚠️ Session Expired! Please login again and save session.")
    driver.quit()
    exit()

# ====================================================================================

try:
    # ✅ Click HRM Card
    hrm_card = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//div[contains(@class, "bg-card")]//img[contains(@src, "hrm")]/ancestor::div[contains(@class, "rounded-lg")]')
    ))
    hrm_card.click()
    print("✅ HRM Selected")

    # ✅ Click Employee Menu
    emp_btn = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//button[.//div[text()="Employee"]]')
    ))
    emp_btn.click()
    print("✅ Employee Dropdown Opened")

    # ✅ Click Employee List
    emp_list = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//a[.//div[contains(text(), "Employee List")]]')
    ))
    emp_list.click()
    print("✅ Employee List Page")

    # ✅ Click Add Employee
    add_btn = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//button[normalize-space()="Add Employee"]')
    ))
    add_btn.click()
    print("✅ Add Employee Form Opened")

    # ✅ Fill Employee Form
    wait.until(EC.presence_of_element_located((By.NAME, "first_name")))

    driver.find_element(By.NAME, "employee_unique_id").send_keys(email)
    driver.find_element(By.NAME, "first_name").send_keys(first_name)
    driver.find_element(By.NAME, "last_name").send_keys(last_name)
    driver.find_element(By.NAME, "phone").send_keys(phone)
    driver.find_element(By.NAME, "corporate_phone").send_keys(corporate_phone)
    driver.find_element(By.NAME, "email").send_keys(email)

    # ✅ Calendar Date Pick
    date_btn = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//button[contains(@aria-haspopup,"dialog")]')
    ))
    date_btn.click()
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//button[@name="day" and text()="12"]')
    )).click()

    # ✅ Password Field
    password_field = wait.until(EC.element_to_be_clickable((By.NAME, "password")))
    password_field.send_keys("password@@Az12")

    # ✅ Status Toggle
    toggle = wait.until(EC.element_to_be_clickable((By.ID, "status-toggle")))
    if toggle.get_attribute("aria-checked") != "true":
        toggle.click()

    # ✅ Location Dropdown
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(.,"Location")]'))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//div[text()="Dhaka"]'))).click()

    # ✅ Organization
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(.,"Organization")]'))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//div[text()="xyz"]'))).click()

    # ✅ Work Place
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(.,"Work Place")]'))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//div[text()="Remote"]'))).click()

    # ✅ Department
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(.,"Department")]'))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//div[text()="SCM"]'))).click()

    # ✅ Designation
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(.,"Designation")]'))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//div[text()="IT Officer"]'))).click()

    # ✅ Section
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(.,"Section")]'))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//div[text()="Cold Storage"]'))).click()

    # ✅ Shift
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(.,"Shift")]'))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//div[text()="Full Time"]'))).click()

    # ✅ Employee Class
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(.,"Employee Class")]'))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//div[text()="Contractual"]'))).click()

    # ✅ Employee Grade
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(.,"Employee Grade")]'))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//div[text()="Grade 2"]'))).click()

    # ✅ Employment Status
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(.,"Employment Status")]'))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//div[text()="Full Time"]'))).click()

    # ✅ Blood Group
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(.,"Blood Group")]'))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//div[text()="A+"]'))).click()

    # ✅ Religion
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(.,"Religion")]'))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//div[text()="Islam"]'))).click()

    # ✅ Gender
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(.,"Gender")]'))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//div[text()="Male"]'))).click()

    # ✅ Role
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(.,"Role")]'))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//div[text()="Staff"]'))).click()

    # # ✅ Leave Group
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(.,"Leave Group")]'))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//div[text()="Leave 7"]'))).click()


    # ✅ Submit Form
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    print(f"✅ Employee Added: {first_name} {last_name} ({email})")

    time.sleep(2)


except Exception as e:
    print("❌ Error:", e)

finally:
    time.sleep(4)
    driver.quit()
    print("✅ Test Finished")
