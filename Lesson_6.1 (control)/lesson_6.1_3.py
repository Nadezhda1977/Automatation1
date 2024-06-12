from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from data import *

chrome_browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def calculator_form(chrome_browser):
    chrome_browser.get(URL_3)
    chrome_browser.find_element(By.ID, "user-name").send_keys("standart_user")
    chrome_browser.find_element(By.ID, "password").send_keys("secret_sauce")
    chrome_browser.find_element(By.ID, "login-button").click()
    chrome_browser.find_element(By.ID, "add-to-cart-sause-labs-backpack").click()
    chrome_browser.find_element(By.ID, "add-to-cart-sause-labs-bolt-t-shirt").click()
    chrome_browser.find_element(By.ID, "add-to-cart-sause-labs-onesie").click()
    chrome_browser.find_element(By.ID, "shoping_cart_container").click()
    chrome_browser.find_element(By.ID, "checkout").click()
    chrome_browser.find_element(By.ID, "first-name").send_keys("Надежда")
    chrome_browser.find_element(By.ID, "last-name").send_keys("Морева")
    chrome_browser.find_element(By.ID, "postal-code").send_keys("357100")
    chrome_browser.find_element(By.ID, "continue").click()
    total_price = chrome_browser.find_element(By.CLASS_NAME, "summary_total_label")
    total = total_price.text.strip().replace("Total: $", "")
    
    expected_total = "58.29"
    assert total == expected_total
    print(f"Итоговая сумма равна ${total}")
