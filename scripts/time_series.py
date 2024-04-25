import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def time_series(region):

    region_1 = pd.read_pickle(os.path.join(BASE_DIR,"notebooks/no_outlier_1.pk1"))

    region_2 = pd.read_pickle(os.path.join(BASE_DIR,"notebooks/no_outlier_2.pk1"))

    region_3 = pd.read_pickle(os.path.join(BASE_DIR,"notebooks/no_outlier_3.pk1"))

    regions = {
        'benin-malanville': region_1, 'sierraleone-bumbuna': region_2, 'togo-dapang_qc': region_3
    }

    region_1["Timestamp"] = pd.to_datetime(region_1['Timestamp'])
    region_2["Timestamp"] = pd.to_datetime(region_2['Timestamp'])
    region_3["Timestamp"] = pd.to_datetime(region_3['Timestamp'])

    hourly = regions[region].set_index('Timestamp')

    # Resample the DataFrame on an hourly basis and calculate the mean
    hourly = hourly.resample('D').mean()

    # Plotting the metrics
    plt.figure(figsize=(15, 10))

    # Plot GHI
    plt.subplot(4, 1, 1)
    sns.lineplot(data=hourly['GHI'], marker='o', color='blue')
    plt.title('Hourly GHI')
    plt.xlabel('Timestamp')
    plt.ylabel('GHI')

    # Plot DNI
    plt.subplot(4, 1, 2)
    sns.lineplot(data=hourly['DNI'], marker='o', color='green')
    plt.title('Hourly DNI')
    plt.xlabel('Timestamp')
    plt.ylabel('DNI')


    # Plot DHI
    plt.subplot(4, 1, 3)
    sns.lineplot(data=hourly['DHI'], marker='o', color='red')
    plt.title('Hourly DHI')
    plt.xlabel('Timestamp')
    plt.ylabel('DHI')

    # Plot Tamb
    plt.subplot(4, 1, 4)
    sns.lineplot(data=hourly['Tamb'], marker='o', color='orange')
    plt.title('Hourly Tamb')
    plt.xlabel('Timestamp')
    plt.ylabel('Tamb')


    plt.tight_layout()
    return plt