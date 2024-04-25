import pandas as pd
import matplotlib.pyplot as plt
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def temprature(region):

    region_1 = pd.read_pickle(os.path.join(BASE_DIR,"notebooks/no_outlier_1.pk1"))

    region_2 = pd.read_pickle(os.path.join(BASE_DIR,"notebooks/no_outlier_2.pk1"))

    region_3 = pd.read_pickle(os.path.join(BASE_DIR,"notebooks/no_outlier_3.pk1"))

    regions = {
        'benin-malanville': region_1, 'sierraleone-bumbuna': region_2, 'togo-dapang_qc': region_3
    }

    region_1["Timestamp"] = pd.to_datetime(region_1['Timestamp'])
    region_2["Timestamp"] = pd.to_datetime(region_2['Timestamp'])
    region_3["Timestamp"] = pd.to_datetime(region_3['Timestamp'])

    regions[region].set_index('Timestamp', inplace=True)

    # Convert 'Timestamp' index to date
    regions[region].index = regions[region].index.date

    # Scatter plot comparing Module Temperatures (TModA, TModB) with Ambient Temperature (Tamb)
    plt.figure(figsize=(8, 6))

    plt.scatter(regions[region]['TModA'], regions[region]['Tamb'], color='b', label='TModA vs Tamb')
    plt.scatter(regions[region]['TModB'], regions[region]['Tamb'], color='r', label='TModB vs Tamb')

    plt.title('Module Temperatures vs Ambient Temperature')
    plt.xlabel('Module Temperature (°C)')
    plt.ylabel('Ambient Temperature (°C)')
    plt.legend()
    plt.grid(True)

    return plt

    
    
