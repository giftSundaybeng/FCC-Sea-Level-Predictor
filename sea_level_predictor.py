import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Load data
    data = pd.read_csv('epa-sea-level.csv')

    # Scatter plot
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'], label='Original Data')

    # Line of best fit (all data)
    slope, intercept, _, _, _ = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    years = pd.Series(range(1880, 2051))
    line = slope * years + intercept
    plt.plot(years, line, color='orange', label='Best Fit Line (1880-2050)')

    # Line of best fit (2000 onward)
    recent_data = data[data['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
    recent_years = pd.Series(range(2000, 2051))
    recent_line = slope_recent * recent_years + intercept_recent
    plt.plot(recent_years, recent_line, color='yellow', label='Best Fit Line (2000-2050)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save and return plot
    plt.savefig('sea_level_plot.png')
    return plt.gca()
