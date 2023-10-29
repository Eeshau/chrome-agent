import selenium
import time
from bs4 import BeautifulSoup

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print(selenium.__version__)  # 4.14.0

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("http://www.dominos.ca/")  # Navigate to a URL

html_content = driver.page_source  # Read HTML content

# Now use BeautifulSoup to parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Example: To find all button elements using BeautifulSoup
buttons = soup.find_all('button')
for btn in buttons:
    print(btn.text)

# Locate an element based on its HTML content and click it
# Using Selenium, as before:
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "home-page-order-online"))
    )
    element.click()
except:
    print("Element not found or other error occurred.")

time.sleep(50)  # This will keep the browser window open for 30 seconds
