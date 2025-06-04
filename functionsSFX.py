import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def button_clicks(driver, xpath_link):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath_link))
    )
    element.click()
    return print("Произошёл клик по элементу button")

def links_click(driver, xpath_link):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath_link))
    )
    element.click()
    return print("Произошло нажатие по ссылке.")

def new_handle_check(driver, handles_before, handles_after, original_handle):
    try:
        if len(handles_after) > len(handles_before):
            new_handle = [h for h in handles_after if h not in handles_before][0]
            driver.switch_to.window(new_handle)

            print(f"\nНовая вкладка открыта:")
            print(f"URL: {driver.current_url}")
            print(f"Title: {driver.title}")

            time.sleep(10)

            # Закрываем новую вкладку
            driver.close()
            driver.switch_to.window(original_handle)
        else:
            print(f"\nСсылка открылась в текущей вкладке: {driver.current_url}")
            time.sleep(1)
    except Exception as e:
        print(str(e))
        time.sleep(30)
    return print("Завершил проверку линков.")

def auto_scroll_to_element(driver, xpath_link):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath_link))
    )

    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)

    return print(f"Прокрутка до элемента с локатором {xpath_link} успешно заверщена.")
