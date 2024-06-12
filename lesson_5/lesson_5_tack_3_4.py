import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
firefox = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

try:
    chrome.get("http://the-internet.herokuapp.com/entry_ad")                                           
    firefox.get("http://the-internet.herokuapp.com/entry_ad")    

    wait = WebDriverWait(chrome, 10)
    wait = WebDriverWait(firefox, 10)
    close_button_chrome = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".modal-footer")))
    time.sleep(3)
    close_button_firefox = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".modal-footer")))
    time.sleep(3)
    close_button_chrome.click()
    time.sleep(2)
    close_button_firefox.click()
    time.sleep(2)


except Exception as ex:
    print(ex)
finally:
    chrome.quit()
    firefox.quit()