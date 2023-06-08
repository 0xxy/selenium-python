from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
  driver = webdriver.Chrome()
  driver.get('https://suninjuly.github.io/math.html')
  
  x_element = driver.find_element(By.ID, 'input_value')
  x = x_element.text
  y = calc(x)

  answer = driver.find_element(By.ID, 'answer')
  answer.send_keys(y)
  checkbox = driver.find_element(By.ID, 'robotCheckbox')
  checkbox.click()
  radioButton = driver.find_element(By.ID, 'robotsRule')
  radioButton.click()
  button = driver.find_element(By.CLASS_NAME, 'btn')
  button.click()

finally:
  time.sleep(5)
  driver.quit()
