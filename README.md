# Travel Data Comparison Web Scraper

This project is a travel data scraper that collects flight and hotel prices from a travel website. The data is stored in an SQLite database and analyzed using pandas. The results are visualized with matplotlib and seaborn, and the data is displayed on a simple Flask web interface.

## Project Structure

- `app.py`: The main Flask application that serves the web interface.
- `scraper.py`: Contains the logic to scrape flight and hotel data from a website.
- `database.py`: Functions for creating the SQLite database and storing/retrieving data.
- `analyze.py`: Data analysis and visualization logic.
- `templates/index.html`: HTML template to display visualizations.

## How to Run

1. Install required packages:
    ```bash
    pip install -r requirements.txt
    ```

2. Run the Flask app:
    ```bash
    python app.py
    ```

3. Open your browser and navigate to `http://127.0.0.1:5000/`.

## Challenges Faced

- Handling dynamic content on the website and scraping the correct data.
- Cleaning the data and handling missing or malformed values.
- Storing the data efficiently in an SQLite database.

## Results

The visualizations show the distribution of flight and hotel prices, allowing users to compare price trends.

