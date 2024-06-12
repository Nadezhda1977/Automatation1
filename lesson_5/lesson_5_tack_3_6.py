from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

chrome_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
firefox_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

chrome_driver.get("http://the-internet.herokuapp.com/login")
firefox_driver.get("http://the-internet.herokuapp.com/login")

# Находим поля ввода и кнопку "Login"
username_input_chrome = chrome_driver.find_element(By.ID, "username")
password_input_chrome = chrome_driver.find_element(By.ID, "password")
login_button_chrome = chrome_driver.find_element(By.TAG_NAME,"button")
username_input_firefox = firefox_driver.find_element(By.ID, "username")
password_input_firefox = firefox_driver.find_element(By.ID, "password")
login_button_firefox = firefox_driver.find_element(By.TAG_NAME,"button")


# Вводим значения в поля
username_input_chrome.send_keys("tomsmith")
sleep(2)
username_input_firefox.send_keys("tomsmith")
sleep(2)
password_input_chrome.send_keys("SuperSecretPassword!")
sleep(2)
password_input_firefox.send_keys("SuperSecretPassword!")
sleep(2)

# Кликаем на кнопку "Login"
login_button_chrome.click()
login_button_firefox.click()

# Закрываем Chrome
chrome_driver.quit()
firefox_driver.quit()