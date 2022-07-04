from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    site = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()

    browser.get(site)
    price = browser.find_element(By.ID, 'price')

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))

    browser.find_element(By.ID, 'book').click()

    answer = browser.find_element(By.ID, 'input_value').text
    browser.find_element(By.ID, 'answer').send_keys(calc(answer))
    browser.find_element(By.ID, 'solve').click()



finally:
    time.sleep(10)
    browser.quit()
