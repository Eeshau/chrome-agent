import selenium
import time
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import anthropic
from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT


load_dotenv()  # Load the .env file
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
client = anthropic.Client()  # Removed the ANTHROPIC_API_KEY argument

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("http://www.dominos.ca/")  # Navigate to a URL

html_content = driver.page_source  # Read HTML content


anthropic = Anthropic()
completion = anthropic.completions.create(
    model="claude-2",
    max_tokens_to_sample=30000,
    prompt=f"{HUMAN_PROMPT} given the following html:\n{html_content}\nfind the segment that corresponds to the pizza order button and respond with ONLY the name of the element to feed it into a selenium webdriver {AI_PROMPT}",
    temperature=0.1
)





print(completion.completion)