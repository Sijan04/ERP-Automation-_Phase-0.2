# destroy_session_after_logout.py

import json, time, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://amarsolution.xyz/")
driver.maximize_window()

try:
    #Try load saved LocalStorage session

    with open("localstorage.json", "r") as f:
        session_data = json.load(f)

    for key, value in session_data.items():
        driver.execute_script(f"localStorage.setItem('{key}', '{value}');")

    print("🔐 Session restored!")
    driver.refresh()  #Apply changes

except:
    print("No existing session found! Logging in required!")
    driver.quit()
    exit()

#  Wait dashboard load after refresh

WebDriverWait(driver, 2).until(
    EC.visibility_of_element_located((By.XPATH, '//div[contains(text(), "HRM")]'))
)
print("Dashboard loaded!")



# Click profile logout button to open-menu

profile_img = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//img[@alt='Picture']"))
)
profile_img.click()
time.sleep(1)

# Click Logout button

logout_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Log Out')]"))
)
logout_btn.click()

print("Logout Successfully!")



# Destroy browser session

driver.delete_all_cookies()
driver.execute_script("localStorage.clear();")
print(" Browser session cleared in browser!")

#  Remove saved session files

for file in ["cookies.json", "localstorage.json"]:
    if os.path.exists(file):
        os.remove(file)
        print(f" Deleted: {file}")

print(" Session Fully Destroyed!Need again to login")

driver.quit()
