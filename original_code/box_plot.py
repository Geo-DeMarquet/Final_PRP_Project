from test_dataframe import *

rates_columns = [
    'Mixed anxiety depression-Rates per 1000 population',
    'All phobias-Rates per 1000 population',
    'Obsessive compulsive disorder-Rates per 1000 population',
    'Panic disorder-Rates per 1000 population',
    'Generalised anxiety disorder-Rates per 1000 population',
    'Depressive episode-Rates per 1000 population'
]

excluded_codes = ['A', 'B', 'D', 'E', 'F', 'G', 'H', 'J', 'K', '921'] #excluded due to representing an area (north, east etc. rather than a borough)
filtered_data = health_data[~health_data['Code'].isin(excluded_codes)] #filters data to only include boroughs

plt.figure(figsize=(14, 8))

data_to_plot = [filtered_data[column] for column in rates_columns]

plt.boxplot(data_to_plot, labels=[column.replace('-Rates per 1000 population', '') for column in rates_columns])

plt.title('Comparison of Disorder Rates Across Boroughs')
plt.xlabel('Disorder')
plt.ylabel('Rates per 1000 Population')

plt.tight_layout()
plt.show()