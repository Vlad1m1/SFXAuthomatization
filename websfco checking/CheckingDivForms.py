import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

try:
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.maximize_window()

    with open("RedSiteURLS.txt", 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file]

    for i in range(len(lines)):
        driver.get(lines[i])
        time.sleep(2)
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='order-form-wrap']"))
        )
        time.sleep(2)
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
        time.sleep(15)
except Exception as e:
    print(str(e))
finally:
    print("Power off...")