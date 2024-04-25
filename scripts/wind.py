import pandas as pd
import matplotlib.pyplot as plt
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def wind(region):

    region_1 = pd.read_pickle(os.path.join(BASE_DIR,"notebooks/no_outlier_1.pk1"))

    region_2 = pd.read_pickle(os.path.join(BASE_DIR,"notebooks/no_outlier_2.pk1"))

    region_3 = pd.read_pickle(os.path.join(BASE_DIR,"notebooks/no_outlier_3.pk1"))

    regions = {
        'benin-malanville': region_1, 'sierraleone-bumbuna': region_2, 'togo-dapang_qc': region_3
    }

    fig, axs = plt.subplots(2, 2, figsize=(14, 10))

    # Plot Wind Speed (WS)
    axs[0, 0].plot(regions[region].index, regions[region]['WS'], marker='o', linestyle='-', color='b')
    axs[0, 0].set_title('Wind Speed (WS)')
    axs[0, 0].set_xlabel('Time')
    axs[0, 0].set_ylabel('WS (m/s)')

    # Plot Wind Gust (WSgust)
    axs[0, 1].plot(regions[region].index, regions[region]['WSgust'], marker='o', linestyle='-', color='r')
    axs[0, 1].set_title('Wind Gust (WSgust)')
    axs[0, 1].set_xlabel('Time')
    axs[0, 1].set_ylabel('WSgust (m/s)')

    # Plot Wind Speed Standard Deviation (WSstdev)
    axs[1, 0].plot(regions[region].index, regions[region]['WSstdev'], marker='o', linestyle='-', color='g')
    axs[1, 0].set_title('Wind Speed Std Deviation (WSstdev)')
    axs[1, 0].set_xlabel('Time')
    axs[1, 0].set_ylabel('WSstdev (m/s)')

    # Plot Wind Direction (WD)
    axs[1, 1].plot(regions[region].index, regions[region]['WD'], marker='o', linestyle='-', color='purple')
    axs[1, 1].set_title('Wind Direction (WD)')
    axs[1, 1].set_xlabel('Time')
    axs[1, 1].set_ylabel('WD (degrees)')

    # Adjust layout
    plt.tight_layout()

    return plt