import pandas as pd
import matplotlib.pyplot as plt #importing relevant libraries

def test_bar_chart():
    health_data = pd.read_csv('mental_health.csv') #import for a contained test

    excluded_codes = ['A', 'B', 'D', 'E', 'F', 'G', 'H', 'J', 'K', '921']
    filtered_data = health_data[~health_data['Code'].isin(excluded_codes)] 
#filters data based on codes indicative of boroughs (excludes generalised areas such as north, east etc)
    rates_columns = ['Mixed anxiety depression-Rates per 1000 population',
                     'All phobias-Rates per 1000 population',
                     'Obsessive compulsive disorder-Rates per 1000 population',
                     'Panic disorder-Rates per 1000 population',
                     'Generalised anxiety disorder-Rates per 1000 population', 
                     'Depressive episode-Rates per 1000 population']

    plt.figure(figsize=(14, 8)) #figure dimensions

    bottom = 0

    for column in rates_columns: #creates a stacked bar chart
        plt.bar(filtered_data['Area'], 
                filtered_data[column], 
                bottom=bottom, 
                alpha=0.8, 
                label=column.replace('-Rates per 1000 population', ''))
        bottom = filtered_data[column] if bottom is None else bottom + filtered_data[column]

    plt.legend(title='Disorders', loc='upper left', bbox_to_anchor=(1.05, 1))
    plt.title('Comparison of Disorder Rates Across Boroughs')
    plt.xlabel('Borough') #labels to enhance figure
    plt.ylabel('Rates per 1000 Population')
    plt.xticks(rotation=90)  #rotated for label readability
    plt.tight_layout()

    plt.savefig('bar_chart_output.png') #saves figure (see circleCI file for artifact path)

    plt.close()
    #inclusion of an assertion
    assert filtered_data is not None and not filtered_data.empty, "Filtered data is empty"
    #success nessage
    print("Bar chart has been saved successfully as 'bar_chart_output.png'.")

