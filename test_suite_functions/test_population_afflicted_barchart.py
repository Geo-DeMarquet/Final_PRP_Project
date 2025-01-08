import pandas as pd
import matplotlib.pyplot as plt

def test_population_disorder():

    health_data = pd.read_csv('mental_health.csv') # Load the dataset
    
    # Define the codes to include (codes for all of the regions in UK)
    included_codes = ['A', 'B', 'D', 'E', 'F', 'G', 'H', 'J', 'K']
    filtered_data = health_data[health_data['Code'].isin(included_codes)]
    
    plt.figure(figsize=(12, 6))
    
    x = filtered_data['Area']
    bar_width = 0.5  
    
    plt.bar(x, filtered_data['Population 16-74'], 
            width=bar_width, label='Population', alpha=0.7)
    
    plt.bar(x, filtered_data['Any neurotic disorder-Estimated cases'], width=bar_width, label='Neurotic Disorder Cases', alpha=0.7, color='orange')
    #orange and blue is effective for colourblind people reading the report

    plt.xlabel('Area')
    plt.ylabel('Counts')
    plt.title('Population vs Any Neurotic Disorder Estimated Cases')
    plt.xticks(rotation=90) #stylisation + readability
    plt.legend()
    plt.tight_layout()
    plt.show()
    
    plt.savefig('population_vs_disorder.png')

    print("Bar chart saved as 'population_vs_disorder.png'") #pathing to artifact found in CircleCI yml
    
    plt.close()
    