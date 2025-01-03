from dataframe import *

excluded_codes = ['A', 'B', 'D', 'E', 'F', 'G', 'H', 'J', 'K', '921'] #excluded due to representing an area (north, east etc. rather than a borough)
filtered_data = health_data[~health_data['Code'].isin(excluded_codes)] #filters data to only include boroughs

rates_columns = ['Mixed anxiety depression-Rates per 1000 population', #list of columns to include
                 'All phobias-Rates per 1000 population',
                 'Obsessive compulsive disorder-Rates per 1000 population',
                 'Panic disorder-Rates per 1000 population',
                 'Generalised anxiety disorder-Rates per 1000 population', 
                 'Depressive episode-Rates per 1000 population']

plt.figure(figsize=(14, 8))
bottom = None

for column in rates_columns:
    plt.bar(filtered_data['Area'], 
            filtered_data[column], 
            bottom=bottom, #bottom parameter ensures that the bars for each disorder rate are stacked on top of each other
            alpha=0.8, 
            label=column.replace('-Rates per 1000 population', ''))
    bottom = filtered_data[column] if bottom is None else bottom + filtered_data[column]

plt.legend(title='Disorders', loc='upper left', bbox_to_anchor=(1.05, 1)) #sets co-ordinates for legend

plt.title('Comparison of Disorder Rates Across Boroughs')
plt.xlabel('Borough')
plt.ylabel('Rates per 1000 Population')
plt.xticks(rotation=90) #rotation = 90 for visibility and readability
plt.tight_layout()
plt.show()