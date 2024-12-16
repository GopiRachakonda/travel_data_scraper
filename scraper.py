import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

def scrape_data_selenium():
    # Set up Chrome options for Selenium WebDriver
    chrome_options = Options()
    # Disable headless mode to see the browser (if you want the browser to be visible)
    # chrome_options.add_argument("--headless")  # Uncomment to run in headless mode

    # Automatically download and set up ChromeDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    # URL to scrape
    url = "https://www.booking.com/"  # Replace with the actual website URL
    driver.get(url)

    # Wait for specific elements to load (you can replace the selector with one that matches your site)
    try:
        # Wait until flight prices are visible (adjust according to your site)
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'flight-price'))  # Adjust for the actual page structure
        )
    except Exception as e:
        print("Error while waiting for elements:", e)
        driver.quit()
        return [], []

    # Wait for the page to fully load (add an extra wait time)
    time.sleep(5)  # Increase this wait if the page still doesn't load

    # Get the page source after it has fully loaded
    page_source = driver.page_source

    if not page_source:
        print("Failed to get page source")
        driver.quit()
        return [], []

    # Parse the page with BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Example: Find all elements with the class "flight-price" and "hotel-price"
    flights = soup.find_all('div', class_='flight-price')
    hotels = soup.find_all('div', class_='hotel-price')

    flight_data = []
    hotel_data = []

    # Extracting flight prices (update these according to the actual HTML structure)
    for flight in flights:
        flight_name = flight.find('span', class_='flight-name').text if flight.find('span', class_='flight-name') else 'N/A'
        flight_price = flight.find('span', class_='price').text if flight.find('span', class_='price') else 'N/A'
        flight_data.append({'flight_name': flight_name, 'price': flight_price})

    # Extracting hotel prices (update these according to the actual HTML structure)
    for hotel in hotels:
        hotel_name = hotel.find('span', class_='hotel-name').text if hotel.find('span', class_='hotel-name') else 'N/A'
        hotel_price = hotel.find('span', class_='price').text if hotel.find('span', class_='price') else 'N/A'
        hotel_data.append({'hotel_name': hotel_name, 'price': hotel_price})

    # Close the driver after scraping
    driver.quit()

    return flight_data, hotel_data

if __name__ == "__main__":
    # Call the function to scrape data
    flight_data, hotel_data = scrape_data_selenium()

    # Print out the scraped data
    print("Flight Data:", flight_data)
    print("Hotel Data:", hotel_data)
