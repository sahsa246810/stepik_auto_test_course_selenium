
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"

browser.get(link)

try:
    firstname= browser.find_element(By.NAME, "firstname")
    firstname.send_keys("Борис")
    lastname= browser.find_element(By.NAME, "lastname")
    lastname.send_keys("Борись")
    email = browser.find_element(By.NAME, "email")
    email.send_keys("dokonca@mail.ru")
    
    file_cl = browser.find_element(By.ID, "file")
    dir = os.path.abspath(os.path.dirname(__file__))
    dir_file = os.path.join(dir, "file.txt")
    file_cl.send_keys(dir_file)
    submit = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    submit.click()
finally:
    time.sleep(30)
    browser.quit()