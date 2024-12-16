import os
import matplotlib.pyplot as plt
import numpy as np
from flask import Flask, render_template, send_from_directory

# Set Matplotlib to use a non-interactive backend
import matplotlib

matplotlib.use('Agg')  # Use 'Agg' backend to prevent GUI errors

# Dummy data for flight prices and hotel prices
flight_prices = np.random.uniform(100, 1000, 500)  # Random flight prices between $100 and $1000
hotel_prices = np.random.uniform(50, 800, 500)  # Random hotel prices between $50 and $800

app = Flask(__name__)

# Ensure the static directory exists to save the images
os.makedirs('static', exist_ok=True)


def create_and_save_plots():
    # Flight price distribution plot
    fig1, ax1 = plt.subplots(figsize=(6, 4))  # Smaller plot size for flight prices
    ax1.hist(flight_prices, bins=10, color='skyblue', edgecolor='black')
    ax1.set_title('Flight Price Distribution')
    ax1.set_xlabel('Flight Price ($)')
    ax1.set_ylabel('Frequency')

    # Save the flight price plot
    flight_plot_path = 'static/flight_price_plot.png'
    fig1.savefig(flight_plot_path, dpi=100)  # Save flight price plot

    # Hotel price distribution plot
    fig2, ax2 = plt.subplots(figsize=(6, 4))  # Smaller plot size for hotel prices
    ax2.hist(hotel_prices, bins=10, color='lightgreen', edgecolor='black')
    ax2.set_title('Hotel Price Distribution')
    ax2.set_xlabel('Hotel Price ($)')
    ax2.set_ylabel('Frequency')

    # Save the hotel price plot
    hotel_plot_path = 'static/hotel_price_plot.png'
    fig2.savefig(hotel_plot_path, dpi=100)  # Save hotel price plot

    return flight_plot_path, hotel_plot_path


@app.route('/')
def index():
    # Generate and save the plots
    flight_plot, hotel_plot = create_and_save_plots()

    # Render the template and pass the plot paths
    return render_template('index.html', flight_plot=flight_plot, hotel_plot=hotel_plot)


@app.route('/static/<filename>')
def send_plot(filename):
    return send_from_directory('static', filename)


if __name__ == "__main__":
    app.run(debug=True)

