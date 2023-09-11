import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def cal(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"

browser.get(link)

try:
    pochti_alert = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    pochti_alert.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x_el = browser.find_element(By.ID, "input_value")
    x = x_el.text
    y = cal(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    submit = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    submit.click()
finally:
    time.sleep(10)
    browser.quit()