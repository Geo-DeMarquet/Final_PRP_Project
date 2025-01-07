import pandas as pd
import matplotlib.pyplot as plt #import libraries

def test_box_plot(): #defines test function

    health_data = pd.read_csv('mental_health.csv') #reads in csv for contained test

    rates_columns = [
        'Mixed anxiety depression-Rates per 1000 population',
        'All phobias-Rates per 1000 population',
        'Obsessive compulsive disorder-Rates per 1000 population',
        'Panic disorder-Rates per 1000 population',
        'Generalised anxiety disorder-Rates per 1000 population',
        'Depressive episode-Rates per 1000 population'
    ]

    excluded_codes = ['A', 'B', 'D', 'E', 'F', 'G', 'H', 'J', 'K', '921']  # excluded due to representing an area (north, east etc. rather than a borough)
    filtered_data = health_data[~health_data['Code'].isin(excluded_codes)]  # filters data to only include boroughs

    plt.figure(figsize=(14, 8)) #figure dimensions

    data_to_plot = [filtered_data[column] for column in rates_columns]
    #label and readability improvements
    plt.boxplot(data_to_plot, labels=[column.replace('-Rates per 1000 population', '') for column in rates_columns])

    plt.title('Comparison of Disorder Rates Across Boroughs')
    plt.xlabel('Disorder')
    plt.ylabel('Rates per 1000 Population')

    plt.tight_layout()

    plt.savefig('box_plot_output.png') #saves figure (see circleCI yml file for artifact pathing)

    plt.close()

    assert filtered_data is not None and not filtered_data.empty, "Filtered data is empty"
    #assertion inclusion & success message
    print("Boxplot has been saved as 'box_plot_output.png'.")
