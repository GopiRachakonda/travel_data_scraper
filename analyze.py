import os
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Use a non-GUI backend
import matplotlib.pyplot as plt
from flask import Flask, render_template

app = Flask(__name__)

# Sample data
flight_data = pd.DataFrame({
    'price': [100, 200, 150, 300, 400, 250, 350, 120, 180, 220],
    'flight_name': ['Flight A', 'Flight B', 'Flight C', 'Flight D', 'Flight E',
                    'Flight F', 'Flight G', 'Flight H', 'Flight I', 'Flight J']
})

# Function to create and save plot
def create_and_save_plot(flight_data):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.hist(flight_data['price'], bins=10, alpha=0.7)
    ax.set_title('Flight Price Distribution')
    ax.set_xlabel('Price')
    ax.set_ylabel('Frequency')

    # Save the plot as a static image file
    plot_path = 'static/flight_price_plot.png'
    fig.savefig(plot_path)  # Save plot to static folder
    plt.close(fig)  # Close the plot to free memory
    return plot_path

@app.route('/')
def index():
    # Create and save the plot
    plot_path = create_and_save_plot(flight_data)

    return render_template('index.html', plot_path=plot_path)

if __name__ == '__main__':
    app.run(debug=True)
