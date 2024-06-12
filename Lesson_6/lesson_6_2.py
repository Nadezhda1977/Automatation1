from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    browser.get("http://uitestingplayground.com/textinput")
    button = browser.find_element(By.CSS_SELECTOR, "#newButtonName").send_keys("SkyPro")
    my_button_name = browser.find_element(By.CSS_SELECTOR, "#updatingButton").click()
    new_button_name = browser.find_element(By.CSS_SELECTOR, "#updatingButton").text
    print(new_button_name)

except Exception as ex:
    print(ex)
finally:
    browser.quit()