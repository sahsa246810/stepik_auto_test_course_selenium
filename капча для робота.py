import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def cal(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
link = "https://suninjuly.github.io/math.html"

browser.get(link)

try:
    x_el = browser.find_element(By.ID, "input_value")
    x = x_el.text
    y = cal(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    radio = browser.find_element(By.ID, "robotsRule")
    radio.click()
    submit = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    submit.click()
finally:
    time.sleep(30)
    browser.quit()