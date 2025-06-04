import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager as FirefoxDriverManager

try:
    service = FirefoxService(FirefoxDriverManager().install())
    driver = webdriver.Firefox(service=service)

    driver.maximize_window()
    driver.get("http://1-cfresh.ru/")

    time.sleep(3)
    shapka = driver.find_elements("xpath", "//div[@class='header-links']/*")
    for i in range(len(shapka)):
        link = driver.find_element("xpath", f"//div[2]/a[{i + 1}]")
        link.click()
        time.sleep(10)
        print(f"Текущая вкладка: {driver.title}")
        print(f"Текущий URL: {driver.current_url}")
        driver.back()
        time.sleep(2)
except Exception as e:
    print(str(e))
finally:
    print("Тестирование завершено.")
    driver.quit()