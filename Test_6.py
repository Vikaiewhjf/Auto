from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

link = "https://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    treasure_img = browser.find_element(By.ID, "input_value")
    x_value = treasure_img.text
    x = int(x_value) 

    calc = math.log(abs(12 * math.sin(x)))

    element1 = browser.find_element(By.ID, "answer")
    element1.send_keys(str(calc))

    element2 = browser.find_element(By.ID, "robotCheckbox")
    element2.click()

    element3 = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("arguments[0].scrollIntoView(true);", element3)
    element3.click()

    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    browser.execute_script("arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()  