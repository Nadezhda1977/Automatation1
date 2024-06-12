from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

chrome_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
firefox_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

chrome_driver.get("http://the-internet.herokuapp.com/inputs")
firefox_driver.get("http://the-internet.herokuapp.com/inputs")

# Находим поле ввода
input_field_chrome = chrome_driver.find_element(By.TAG_NAME, "input")
input_field_firefox = firefox_driver.find_element(By.TAG_NAME, "input")
# Вводим значение "1000"
input_field_chrome.send_keys("1000")
sleep(2)
input_field_firefox.send_keys("1000")
sleep(2)

# Очищаем поле ввода
input_field_chrome.clear()
sleep(2)
input_field_firefox.clear()
sleep(2)

# Вводим значение "999"
input_field_chrome.send_keys("999")
sleep(2)
input_field_firefox.send_keys("999")
sleep(2)

# Закрываем Chrome
chrome_driver.quit()
firefox_driver.quit()