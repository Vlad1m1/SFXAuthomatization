import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

try:
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    with open("RedSiteURLS.txt", 'r', encoding='utf-8') as file:
        urls = [line.strip() for line in file if line.strip()]

    for url in urls:
        driver.get(url)
        original_handle = driver.current_window_handle

        # Ожидание и работа с формой
        form = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='order-form-wrap']")))
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", form)
        time.sleep(5)

        # Проверка отправки формы
        try:
            submit_btn = wait.until(EC.presence_of_element_located(
                (By.XPATH, "//*[@id='form-order']/div/div[2]/div[2]/div[2]/input")))
            submit_btn.click()
            print("Проверка на отправку без галочки. Ожидаемый результат: не отправилось.")
            time.sleep(5)

            checkbox = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//input[@class='order-form__agree_checkbox sfx-error']")))
            checkbox.click()
            submit_btn.click()
            print("Проверка на отправку без других важных полей. Ожидаемый результат: не отправилось.")
            time.sleep(5)
        except Exception as e:
            print(f"Ошибка при работе с формой: {str(e)}")

        # Улучшенная проверка ссылок
        doc_links = [
            "//a[@href='/wp-content/uploads/СогласиеСЭ.doc']",
            "//a[@href='/wp-content/uploads/agree.pdf']"
        ]

        for link_xpath in doc_links:
            try:
                # Запоминаем количество открытых вкладок до клика
                handles_before = driver.window_handles

                # Находим и кликаем по ссылке
                link = wait.until(EC.element_to_be_clickable((By.XPATH, link_xpath)))
                link.click()
                time.sleep(2)  # Даем время для открытия

                # Проверяем открытие новой вкладки
                handles_after = driver.window_handles

                if len(handles_after) > len(handles_before):
                    new_handle = [h for h in handles_after if h not in handles_before][0]
                    driver.switch_to.window(new_handle)

                    print(f"\nНовая вкладка открыта:")
                    print(f"URL: {driver.current_url}")
                    print(f"Title: {driver.title}")

                    # Закрываем новую вкладку
                    driver.close()
                    driver.switch_to.window(original_handle)
                else:
                    print(f"\nСсылка открылась в текущей вкладке: {driver.current_url}")
                    time.sleep(1)

            except Exception as e:
                print(f"\nОшибка при проверке ссылки {link_xpath}: {str(e)}")
                time.sleep(30)
                continue

except Exception as e:
    print(f"\nПроизошла критическая ошибка: {str(e)}")
    # Создаем скриншот для отладки
    driver.save_screenshot('error_screenshot.png')

finally:
    if 'driver' in locals():
        driver.quit()
    print("\nТестирование завершено. Браузер закрыт.")