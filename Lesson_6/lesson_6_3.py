from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
wait = WebDriverWait(browser, 30)

try:
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#text"), 'Done!'))
    get_attribute = browser.find_element(By.CSS_SELECTOR, "#award").get_attribute("src")
    print(get_attribute)
        
except Exception as ex:
    print(ex)
finally:
    browser.quit()