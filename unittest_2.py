from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        browser = webdriver.Chrome()
        browser.get('http://suninjuly.github.io/registration1.html')

        first_input = browser.find_element(By.CSS_SELECTOR, '.first_block .first')
        first_input.send_keys('Ivan')
        last_name = browser.find_element(By.CSS_SELECTOR, '.first_block .second')
        last_name.send_keys('Ivanov')
        email = browser.find_element(By.CSS_SELECTOR, '.first_block .third')
        email.send_keys('ivan@mail.ru')
        phone = browser.find_element(By.CSS_SELECTOR, '.second_block .first')
        phone.send_keys(375291112233)
        address = browser.find_element(By.CSS_SELECTOR, '.second_block .second')
        address.send_keys('Minsk')
        
        button = browser.find_element(By.CLASS_NAME, 'btn')
        button.click()

        time.sleep(5)
        browser.quit()

    def test_abs2(self):
        browser = webdriver.Chrome()
        browser.get('http://suninjuly.github.io/registration2.html')

        first_input = browser.find_element(By.CSS_SELECTOR, '.first_block .first')
        first_input.send_keys('Ivan')
        last_name = browser.find_element(By.CSS_SELECTOR, '.first_block .second')
        last_name.send_keys('Ivanov')
        email = browser.find_element(By.CSS_SELECTOR, '.first_block .third')
        email.send_keys('ivan@mail.ru')
        phone = browser.find_element(By.CSS_SELECTOR, '.second_block .first')
        phone.send_keys(375291112233)
        address = browser.find_element(By.CSS_SELECTOR, '.second_block .second')
        address.send_keys('Minsk')

        button = browser.find_element(By.CLASS_NAME, 'btn')
        button.click()

        time.sleep(5)
        browser.quit()
        
if __name__ == "__main__":
    unittest.main()