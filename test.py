from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

# Automatically install and use ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL of the page to scrape
url = 'https://www.booking.com/searchresults.html?label=gog235jc-1DCAIoqwFCAm5wSDNYA2irAYgBAZgBMbgBB8gBDNgBA-gBAfgBAogCAagCA7gC2pfVvQbAAgHSAiRiZGI0YzY4Yi01YzEyLTRiMWUtOTA0OS1hYjg5OWE5Zjk0MDjYAgTgAgE&sid=758c99db86de9f8c3bd29999ffd04224&aid=356980&city=-1022488'

# Open the URL using Selenium
driver.get(url)

# Wait for the page to load initially
time.sleep(5)

# Scroll down to load more hotels
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # Scroll down to the bottom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(15)  # Wait for new hotels to load

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    try:
        show_all_link = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "a83ed08757 c21c56c305 bf0537ecb5 f671049264 af7297d90d c0e0affd09"))
    )
        show_all_link.click()
        print('next page')
    except:
        # If no more pages, break the loop
        print("No more pages to load.")
    if new_height == last_height:
        break  # Exit the loop if no more hotels are loaded
    last_height = new_height
    try:
        show_all_link = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "a83ed08757 c21c56c305 bf0537ecb5 f671049264 af7297d90d c0e0affd09"))
        )
        show_all_link.click()
    except:
        # If no more pages, break the loop
        print("No more pages to load.")
        break

# Get the page source and parse it with BeautifulSoup
html_text = driver.page_source
soup = BeautifulSoup(html_text, 'lxml')

# Find hotel elements
hotels = []
hotel_elements = soup.find_all("div", class_="c82435a4b8 a178069f51 a6ae3c2b40 a18aeea94d d794b7a0f7 f53e278e95 c6710787a4")
print(f"Number of hotel elements found: {len(hotel_elements)}")

# Extract hotel names and ratings
for hotel in hotel_elements:
    try:
        name = hotel.find('div', class_="f6431b446c a15b38c233").text.strip()
        rating = hotel.find('div', class_="a3b8729ab1 d86cee9b25").text.strip()
        hotels.append({
            'Hotel Name': name,
            'Rating': rating
        })
    except AttributeError:
        # Skip if any element is not found
        continue

# Create a DataFrame and print it
df = pd.DataFrame(hotels)
print(df)

# Close the browser
driver.quit()