from selenium.webdriver.common.by import By
import time

def test_find_card_button(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    length = len(browser.find_elements(By.CLASS_NAME, "btn-add-to-basket"))

    assert length > 0

    time.sleep(10)