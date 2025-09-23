from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

link = "https://suninjuly.github.io/math.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_el = browser.find_element(By.ID, "input_value")
    x = int(x_el.text)
    
    calc = math.log(math.fabs(12* math.sin(x)))

    element1 = browser.find_element(By.ID, "answer")
    element1.send_keys(str(calc))

    element2 = browser.find_element(By.CLASS_NAME, "form-check-input")
    element2.click()

    element3 = browser.find_element(By.ID, "robotsRule")
    element3.click()

    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()