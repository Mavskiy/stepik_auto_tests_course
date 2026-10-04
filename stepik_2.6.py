import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = None
try:
    browser = webdriver.Chrome()

    url = "https://suninjuly.github.io/explicit_wait2.html"
    browser.get(url)


    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    book_button = browser.find_element(By.ID, "book")
    book_button.click()

    browser.execute_script("window.scrollBy(0, 200);")

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text

    y = calc(x)

    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(y)

    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()

    time.sleep(10)

finally:
    if browser:
        browser.quit()
