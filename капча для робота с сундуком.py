from math import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
    return log(abs(12 * sin(int(x))))

try:
    browser.get(link)
    el = browser.find_element(By.ID, "treasure")
    x = el.get_attribute("valuex")
    input = browser.find_element(By.ID, "answer")
    input.send_keys(calc(x))
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    radio = browser.find_element(By.ID, "robotsRule")
    radio.click()
    submit = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    submit.click()
finally:
    time.sleep(50)
    browser.quit()