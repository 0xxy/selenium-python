from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x): 
  return str(math.log(abs(12*math.sin(int(x)))))

try:
  browser = webdriver.Chrome()
  browser.get('http://suninjuly.github.io/explicit_wait2.html')

  btn = browser.find_element(By.ID, 'book')
  browser.execute_script("return arguments[0].scrollIntoView(true);", btn)

  WebDriverWait(browser, 10).until(
    EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
  )
  
  btn.click()

  x = browser.find_element(By.ID, 'input_value')
  x_val = x.text
  y = calc(x_val)

  answer = browser.find_element(By.ID, 'answer')
  answer.send_keys(y)
  button = browser.find_element(By.ID, 'solve')
  button.click()

  # alert_obj = browser.switch_to.alert
  # msg = alert_obj.text
  # print(msg)
finally:
  time.sleep(15)
  browser.quit()