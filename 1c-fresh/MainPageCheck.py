import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager as FirefoxDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def link_click(xpath_locator):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath_locator))
    )

try:
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.get("http://1-cfresh.ru")
    time.sleep(5)
    buttons = driver.find_elements("xpath", "//div[@class='first-foot']/*")
    time.sleep(5)

    links = {
        "//*[@id='registerForm']/div[3]/div[1]/label/a[1]"
        "//*[@id='registerForm']/div[3]/div[1]/label/a[2]"
    }

except Exception as e:
    print(str(e))

finally:
    driver.quit()
    print("Тестирование завершено.")