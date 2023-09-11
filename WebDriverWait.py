from selenium import webdriver
from selenium.webdriver.common.by import By
from math import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

def calc(x):
    return log(abs(12 * sin(int(x))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser.get(link)
    button = browser.find_element(By.ID, "book")
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button.click()
    input = browser.find_element(By.ID, "answer")
    x_el = browser.find_element(By.ID, "input_value")
    x = int(x_el.text)
    input.send_keys(calc(x))
    submit = browser.find_element(By.ID, "solve")
    submit.click()
finally:
    time.sleep(10)
    browser.quit()