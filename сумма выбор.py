from math import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:

    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/selects1.html?"
    browser.get(link)

    num1_el = browser.find_element(By.ID, "num1")
    num1 = int(num1_el.text)
    num2_el = browser.find_element(By.ID, "num2")
    num2 = int(num2_el.text)

    summ = num1 + num2
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(summ))
    submit = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    submit.click()
finally:
    time.sleep(30)
    browser.quit()