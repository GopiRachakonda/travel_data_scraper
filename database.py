import sqlite3
from scraper import scrape_data_selenium

# Connect to the SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect('travel_data.db')
cursor = conn.cursor()

# Create tables if they don't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS flights (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    flight_name TEXT,
    price REAL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS hotels (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    hotel_name TEXT,
    price REAL
)
''')

# Scrape the data
flight_data, hotel_data = scrape_data_selenium()

# Insert scraped flight data into the 'flights' table
for flight in flight_data:
    cursor.execute("INSERT INTO flights (flight_name, price) VALUES (?, ?)",
                   (flight['flight_name'], flight['price']))

# Insert scraped hotel data into the 'hotels' table
for hotel in hotel_data:
    cursor.execute("INSERT INTO hotels (hotel_name, price) VALUES (?, ?)",
                   (hotel['hotel_name'], hotel['price']))

# Commit the changes and close the connection
conn.commit()
conn.close()
