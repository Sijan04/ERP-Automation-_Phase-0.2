# #After Login go into the HRM Module after that create class and submit form and add to the list


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
import time

# Setup Faker
fake = Faker()           #Fake data generator add

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

    # Click Employee Classes
    employee_classes_link = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//a[@href="/hrm/employee-classes" and .//div[contains(text(), "Employee Classes")]]')
    ))
    employee_classes_link.click()
    print("✅ Clicked Employee Classes")

    # Click "Add Employee Class" button
    add_class_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//button[contains(., "Add Employee Class")]')
    ))
    add_class_button.click()
    print("✅ Clicked 'Add Employee Class' button")

    # Generate fake employee class name
    fake_class_name = fake.job()   # Example: "Software Engineer"
    # You can also use: fake.word(), fake.company(), etc.

    # Enter the employee class name
    input_field = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//input[@placeholder="Enter employee class name"]')
    ))
    input_field.clear()
    input_field.send_keys(fake_class_name)
    print(f"✅ Entered employee class name: {fake_class_name}")

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
