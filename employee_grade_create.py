


# Employee_Grade_Form_Create

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

    # Click Employee dropdown
    employee_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//button[.//div[text()="Employee"]]')
    ))
    employee_button.click()
    print("✅ Clicked Employee dropdown")

    # Click Employee Grades
    employee_grades_link = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//div[text()="Employee Grades"]/ancestor::a')
    ))
    employee_grades_link.click()
    print("✅ Clicked Employee Grades")

    # Click "Add Employee Grade" button
    add_grade_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//button[contains(., "Add Employee Grade")]')
    ))
    add_grade_button.click()
    print("✅ Clicked Add Employee Grade button")

    # Generate fake name and salaries
    grade_name = fake.job()  # Example: "Software Engineer"
    min_salary = random.randint(20000, 40000)
    max_salary = random.randint(50000, 90000)

    # Enter the grade name
    name_field = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//input[@name="name" and @placeholder="Enter section name"]')
    ))
    name_field.clear()
    name_field.send_keys(grade_name)
    print(f"✅ Entered grade name: {grade_name}")

    # Enter min salary
    min_salary_field = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//input[@name="min_salary"]')
    ))
    min_salary_field.clear()
    min_salary_field.send_keys(str(min_salary))
    print(f"✅ Entered Min Salary: {min_salary}")

    # Enter max salary
    max_salary_field = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//input[@name="max_salary"]')
    ))
    max_salary_field.clear()
    max_salary_field.send_keys(str(max_salary))
    print(f"✅ Entered Max Salary: {max_salary}")

    time.sleep(8)
    # Click Save/Submit button
    submit_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//button[normalize-space(text())="Add"]')
    ))
    submit_button.click()
    print("✅ Submitted Employee Grade form")

except Exception as e:
    print("❌ Error:", e)

time.sleep(25)
# driver.quit()
