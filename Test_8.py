from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    element1 = browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    value = browser.find_element(By.ID, "input_value")
    x_value = value.text
    x = int(x_value) 

    calc = math.log(abs(12 * math.sin(x)))

    element2 = browser.find_element(By.ID, "answer")
    element2.send_keys(str(calc))

    element3 = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()







finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit() 