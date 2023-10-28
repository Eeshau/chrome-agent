import selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the driver (using Chrome in this example)
driver = webdriver.Chrome(executable_path='path_to_chromedriver')  # Replace with the path to your chromedriver

# Navigate to a URL
driver.get('http://example.com')

# Read HTML content
html_content = driver.page_source

# Print the first 1000 characters of the HTML content
print(html_content[:1000])

# Locate an element based on its HTML content and click it
# Example: Let's say there's a button with the text "Click me!", you can locate and click it like:
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[text()='Click me!']"))
    )
    element.click()
except:
    print("Element not found or other error occurred.")

# Close the browser window
driver.quit()
