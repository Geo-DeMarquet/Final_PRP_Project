import pandas as pd
import matplotlib.pyplot as plt

def test_plot_neurotic_disorder_rates():

    health_data = pd.read_csv('mental_health.csv')

    excluded_codes = ['A', 'B', 'D', 'E', 'F', 'G', 'H', 'J', 'K', '921']

    filtered_data = health_data[~health_data['Code'].isin(excluded_codes)]

    assert filtered_data is not None and not filtered_data.empty, "Filtered data is empty"

    plt.figure(figsize=(14, 8))

    plt.plot(filtered_data['Area'], 
             filtered_data['Any neurotic disorder-Rates per 1000 population'], 
             marker='o', color='red', linestyle='')

    for area, rate in zip(filtered_data['Area'], filtered_data['Any neurotic disorder-Rates per 1000 population']):
        plt.vlines(x=area, ymin=0, ymax=rate, colors='gray', alpha=0.5, linestyles='dotted')

    plt.title('Any Disorder Rates Across Boroughs')
    plt.xlabel('Borough')
    plt.ylabel('Rates per 1000 Population')
    plt.xticks(rotation=90)
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()

    plt.savefig('scatter_disorder_plot.png')
    plt.close()

    print("Plot has been saved as 'scatter-disorder_plot.png'.")
