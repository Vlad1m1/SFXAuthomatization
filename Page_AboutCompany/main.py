import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.maximize_window()
driver.get("https://www.sfx-tula.ru/services/")
time.sleep(3)

parent = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/div[2]/div")
direct_children = parent.find_elements(By.XPATH, "./div")
print(f"Найдено прямых кликабельных потомков: {len(direct_children)}")

try:
    for i in range(len(direct_children)):
        now_content = driver.find_element(By.XPATH,
            f"/html/body/div[3]/div/div[1]/div[2]/div/div[{i + 1}]/div[2]/div/div")
        div_children = now_content.find_elements(By.XPATH, "./div")
        for j in range(len(div_children)):
            # сохраняем исходную вкладку
            original_handle = driver.current_window_handle
            element = driver.find_element(By.XPATH,
                f"/html/body/div[3]/div/div[1]/div[2]/div/div[{i + 1}]/div[2]/div/div/div[{j + 1}]")
            time.sleep(2)
            element.click()

            # даём время на открытие вкладки
            time.sleep(2)
            all_handles = driver.window_handles

            if len(all_handles) > 1:
                # определяем новую вкладку
                new_handle = [h for h in all_handles if h != original_handle][0]
                driver.switch_to.window(new_handle)
                print(f"Url новой вкладки: {driver.current_url}")
                print(f"Title новой вкладки: {driver.title}")
                time.sleep(2)

                # закрываем новую и возвращаемся на исходную
                driver.close()
                driver.switch_to.window(original_handle)
                print(f"Вернулись на исходную вкладку: {driver.current_url}")
            else:
                # если вкладка не открылась, остаёмся и идём назад
                print(f"Новая вкладка не открылась.\nТекущий URL: {driver.current_url}\nТекущий title: {driver.title}")
                time.sleep(2)
                driver.back()

except Exception as e:
    print("Ошибка в тесте:", e)

finally:
    print("Завершаю тестирование.")
    driver.quit()