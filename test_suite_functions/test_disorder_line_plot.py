import pandas as pd
import matplotlib.pyplot as plt #import libraries

def test_disorder_line_plot(): #define test function

    health_data = pd.read_csv('mental_health.csv') #import csv to dataframe

    excluded_codes = ['A', 'B', 'D', 'E', 'F', 'G', 'H', 'J', 'K', '921']
    filtered_data = health_data[~health_data['Code'].isin(excluded_codes)]  # filters data to only include boroughs

    trend_disorders = [
        'Mixed anxiety depression-Rates per 1000 population',
        'Generalised anxiety disorder-Rates per 1000 population',
        'Depressive episode-Rates per 1000 population',
        'Obsessive compulsive disorder-Rates per 1000 population',
        'Panic disorder-Rates per 1000 population'
    ]

    plt.figure(figsize=(14, 8))  #figure dimensions

    for disorder in trend_disorders:
        plt.plot(filtered_data['Area'], filtered_data[disorder], label=disorder.split('-')[0])

    plt.title('Trends in Disorder Rates Across Boroughs')
    plt.xlabel('Borough')
    plt.ylabel('Rates per 1000 Population')
    plt.xticks(rotation=90)  #labels and readability enhancements
    plt.legend(title='Disorders')
    plt.grid(True)
    plt.tight_layout()

    plt.savefig('trend_disorder_output.png') #save figure as png, path can be found in CircleCI yml
    plt.close()

    assert filtered_data is not None and not filtered_data.empty, "Filtered data is empty"
    #assertion and success message
    print("Trend plot has been saved as 'trend_plot_output.png'.")
