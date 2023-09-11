from selenium import webdriver
from selenium.webdriver.common.by import By
from math import *
import time

def calc(x):
    return log(abs(12 * sin(int(x))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"

browser.get(link)

try:

    troll = browser.find_element(By.CSS_SELECTOR, ".trollface.btn.btn-primary")
    troll.click()

    time.sleep(5)
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_el = browser.find_element(By.ID, "input_value")
    x = x_el.text
    y = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    submit = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    submit.click()
finally:
    time.sleep(10)
    browser.quit()
