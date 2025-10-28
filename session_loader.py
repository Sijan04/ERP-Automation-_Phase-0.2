# session_loader.py
import json, time
from selenium import webdriver

def load_session():
    driver = webdriver.Chrome()
    driver.get("https://amarsolution.xyz/")
    driver.maximize_window()
    time.sleep(1)

    # Load cookies
    try:
        with open("cookies.json", "r") as f:
            cookies = json.load(f)
        for cookie in cookies:
            cookie.pop('sameSite', None)
            driver.add_cookie(cookie)
        print("🍪 Cookies loaded")
    except:
        print("⚠️ No cookies found")

    driver.refresh()
    time.sleep(1)

    # Load LocalStorage
    try:
        with open("localstorage.json", "r") as f:
            local_data = json.load(f)
        for k, v in local_data.items():
            driver.execute_script(f"localStorage.setItem('{k}','{v}');")
        print("🔐 LocalStorage loaded")
    except:
        print("⚠️ No local storage found")

    driver.refresh()
    print("✅ Session restored!")
    return driver
