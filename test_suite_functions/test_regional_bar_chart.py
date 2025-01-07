import pandas as pd
import matplotlib.pyplot as plt  # Import libraries

def test_bar_plot():  # Defines test function

    health_data = pd.read_csv('mental_health.csv')  # Reads in CSV 

    included_codes = ['A', 'B', 'D', 'E', 'F', 'G', 'H', 'J', 'K', '921']  # Included regions codes
    filtered_data = health_data[health_data['Code'].isin(included_codes)]  # Filters data to only include regions

    disorders = [
        'Any neurotic disorder-Rates per 1000 population',
        'All phobias-Rates per 1000 population',
        'Depressive episode-Rates per 1000 population',
        'Generalised anxiety disorder-Rates per 1000 population',
        'Mixed anxiety depression-Rates per 1000 population'
    ]

    # Plotting the bar chart
    plt.figure(figsize=(25, 10))  # Figure dimensions
    filtered_data.set_index('Area')[disorders].plot(kind='bar', colormap='cividis', alpha=0.8)
    #cividis is beneficial for colourblind readers - important for this plot as there is a wide disparity between some bars

    plt.title('Comparison of Disorder Rates Across Boroughs', fontsize=14)
    plt.xlabel('Region', fontsize=12)
    plt.ylabel('Rates per 1000 Population', fontsize=12)
    plt.xticks(rotation=90)
    plt.legend(title='Disorders prevalence by Region')
    plt.tight_layout()

    plt.savefig('regional_bar_chart.png')  # Saves figure (see CircleCI yml file for artifact pathing)
    plt.close()

    #including an assertion
    assert filtered_data is not None and not filtered_data.empty, "Filtered data is empty"

    print("Bar plot has been saved as 'bar_plot_output.png'.")  # Success message

