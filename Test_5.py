from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

try:
    browser = webdriver.Chrome()
    browser.execute_script("alert('Robots at work');")

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()  