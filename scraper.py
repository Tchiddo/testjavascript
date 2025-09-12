import requests
from bs4 import BeautifulSoup

# 1. Send an HTTP request to the website
url = "https://example.com"
response = requests.get(url)

# Why? -> requests.get() asks the server for the page and returns the HTML content.

# 2. Parse the HTML using BeautifulSoup
soup = BeautifulSoup(response.text, "lxml")

# Why? -> soup turns the messy HTML string into an object we can navigate/search.

# 3. Extract specific elements (like the title)
title = soup.title.text

# Why? -> soup.title finds the <title> tag, and .text gives the inside text.

print("Page title:", title)

import requests

url = "http://quotes.toscrape.com/"
response = requests.get(url)

# Always check if it worked
print("Status code:", response.status_code)
print(response.text[:500])  # print the first 500 characters of the HTML