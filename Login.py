
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# driver = webdriver.Chrome()
# driver.get("https://amarsolution.xyz/login")
# driver.maximize_window()
#
# try:
#     driver.find_element(By.NAME, "email").send_keys("admin@gmail.com")
#     driver.find_element(By.NAME, "password").send_keys("password")
#     driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
# except Exception as e:
#     print("Not login:", e)
#
# # Keep-browser open for 5 minutes
# time.sleep(2)
# driver.quit()



# # login_and_save_session.py
# import json, time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# driver.get("https://amarsolution.xyz/login")
# driver.maximize_window()
#
# try:
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email"))).send_keys("admin@gmail.com")
#     driver.find_element(By.NAME, "password").send_keys("password")
#     driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
#
#     # wait for some element visible after login (adjust as needed)
#     WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body")))
#
#     # Give some time for cookies to be set
#     time.sleep(1)
#
#     # Save cookies to file
#     cookies = driver.get_cookies()  # list of dicts
#     with open("cookies.json", "w") as f:
#         json.dump(cookies, f)
#
#     print("✅ Cookies saved to cookies.json")
# except Exception as e:
#     print("Login failed:", e)
# finally:
#     driver.quit()


# login_and_save_session.py
import json, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://amarsolution.xyz/login")
driver.maximize_window()

try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "email"))
    ).send_keys("admin@gmail.com")

    driver.find_element(By.NAME, "password").send_keys("password")
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




























