from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
wait = WebDriverWait(browser, 20)

try:
    browser.get("http://uitestingplayground.com/ajax")
    blue_button = browser.find_element(By.CSS_SELECTOR, "#ajaxButton").click()
    text_content = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".bg-success"))).text
    print(text_content)
        
except Exception as ex:
    print(ex)
finally:
    browser.quit()
   