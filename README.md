# Booking.com Hotel Scraper

This project is a Python script that scrapes hotel data (name and rating) from Booking.com for a specific city (Pokhara, Nepal). It uses Selenium to automate the browser and BeautifulSoup to parse the HTML content. The scraped data is saved in a CSV file for further analysis.

## Features
- Automates the browser to load all hotel results by clicking the "Load more" button until no more results are available.
- Extracts hotel names and ratings.
- Saves the data to a CSV file (`all_hotels_in_pokhara.csv`).

## Prerequisites

Before running the script, ensure you have the following installed:

1. **Python 3.x**: Download and install Python from [python.org](https://www.python.org/).
2. **ChromeDriver**: The script uses ChromeDriver to automate the Chrome browser. It is automatically installed by the `webdriver_manager` package.
3. **Required Python Packages**: Install the required packages using `pip`.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/prabeshbaral/hotel-scrapping.git
   cd booking-hotel-scraper

### pip install selenium beautifulsoup4 pandas webdriver-manager