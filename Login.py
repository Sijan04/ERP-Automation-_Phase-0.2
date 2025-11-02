

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import json, time, os

# ✅ Load .env
load_dotenv(".env.local")

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
print(EMAIL, PASSWORD)
driver = webdriver.Chrome()
driver.get("https://amarsolution.xyz/login")
driver.maximize_window()

try:
    # Enter email and password from .env
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "email"))
    ).send_keys(EMAIL)

    driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # ✅ Wait until Dashboard loads
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, '//div[contains(text(), "HRM")]'))
    )
    print("✅ Login success!")

    time.sleep(2)

    # ✅ Save Cookies
    with open("cookies.json", "w") as f:
        json.dump(driver.get_cookies(), f, indent=4)

    # ✅ Save LocalStorage tokens
    local_storage = driver.execute_script(
        "var out={}; for(var i=0;i<localStorage.length;i++){"
        "var k=localStorage.key(i); out[k]=localStorage.getItem(k);} return out;"
    )
    with open("localstorage.json", "w") as f:
        json.dump(local_storage, f, indent=4)

    print("📦 Session saved! ✅")

except Exception as e:
    print("Login failed:", e)

finally:
    driver.quit()













