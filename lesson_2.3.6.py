from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select
import os


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    site = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()

    browser.get(site)

    firs_button = browser.find_element(By.XPATH, "//*[@class='trollface btn btn-primary']").click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    text_to_clacl = browser.find_element(By.ID, "input_value").text

    answer = browser.find_element(By.ID, "answer").send_keys(calc(text_to_clacl))
    second_button = browser.find_element(By.XPATH, "//*[@class='btn btn-primary']").click()
    time.sleep(3)
finally:
    time.sleep(10)
    browser.quit()
