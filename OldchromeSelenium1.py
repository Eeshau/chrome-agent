import selenium
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print(selenium.__version__) #4.14.0

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)



driver.get("http:www.dominos.ca/") # Navigate to a URL

html_content = driver.page_source # Read HTML content

# print(html_content[:10000]) # Print the first 10000 characters of the HTML content
print(html_content[:]) # Print the first 10000 characters of the HTML content

#problem html might be wayy to big for a single query -> use chat spliter style code to break it down into 1/5 type
# OR just use beautfiul soup to preprocess the html and get only the buttons, input and text. 

# Locate an element based on its HTML content and click it
# Example: Let's say there's a button with the text "Click me!", you can locate and click it like:
# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, "//button[text()='Delivery']"))
#     )
#     element.click()
# except:
#     print("Element not found or other error occurred.")



time.sleep(30)  # This will keep the browser window open for 10 seconds