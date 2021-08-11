# новый комментари для гита
from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)
time.sleep(3)

button = browser.find_element_by_css_selector(".btn.btn-primary") # находим кнопку по css селектору
button.click() # жмем на кнопку которую нашли
confirm = browser.switch_to.alert  # Находим окно вызова
confirm.accept()  # Соглашаемся или confirm.dismiss() # Не соглашаемся

x_element = browser.find_element_by_id('input_value')
x = x_element.text
inp = calc(x)

input_text = browser.find_element_by_id('answer')
input_text.send_keys(inp)

button = browser.find_element_by_css_selector('.btn.btn-primary')
button.click()
time.sleep(5)

browser.quit()