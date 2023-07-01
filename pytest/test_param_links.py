from selenium.webdriver.common.by import By
import pytest
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.parametrize('link_num', ["895", "896", "897", "898"])
def test_to_login(browser, link_num):
  link = f"https://stepik.org/lesson/236{link_num}/step/1"
  browser.get(link)
  button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, 'ember33')))
  button.click()
  email = browser.find_element(By.ID, 'id_login_email')
  email.send_keys('oksenyuk01@inbox.ru')
  password = browser.find_element(By.ID, 'id_login_password')
  password.send_keys('paragraph1')
  subBtn = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
  subBtn.click()
  time.sleep(10)

  again_btn = browser.find_element(By.CLASS_NAME, 'again-btn')

  if again_btn:
    again_btn.click()
    time.sleep(10)

  answer = str(math.log(int(time.time())))

  input = browser.find_element(By.TAG_NAME, 'textarea')
  WebDriverWait(browser, 5).until(
    EC.visibility_of(input)
  )
  input.send_keys(answer)

  submitBtn = browser.find_element(By.CLASS_NAME, 'submit-submission')
  submitBtn.click()
  time.sleep(5)

  res = browser.find_element(By.CLASS_NAME, 'smart-hints__hint')
  WebDriverWait(browser, 5).until(
    EC.visibility_of(res)
  )
  time.sleep(10)
  result = browser.find_element(By.CLASS_NAME, 'smart-hints__hint').text
  print(result)
  assert "Correct!" == result

