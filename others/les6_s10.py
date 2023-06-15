from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    firstname = browser.find_element(By.CSS_SELECTOR, '.first_block > div:nth-child(1) > input')
    firstname.send_keys('Ivan')
    lastname = browser.find_element(By.CSS_SELECTOR, '.second_class > input[required]')
    lastname.send_keys('Ivanov')
    email = browser.find_element(By.CLASS_NAME, 'third')
    email.send_keys('ivan@mail.ru')
    phone = browser.find_element(By.CSS_SELECTOR, 'input[placeholder*="phone"]')
    phone.send_keys('+375290001122')
    address = browser.find_element(By.CSS_SELECTOR, 'input[placeholder*="address"]')
    address.send_keys('Bel')
    # Отправляем заполненную форму
    time.sleep(1)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()