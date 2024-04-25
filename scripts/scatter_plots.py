import pandas as pd
import matplotlib.pyplot as plt
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def scatter(region):

    region_1 = pd.read_pickle(os.path.join(BASE_DIR,"notebooks/no_outlier_1.pk1"))

    region_2 = pd.read_pickle(os.path.join(BASE_DIR,"notebooks/no_outlier_2.pk1"))

    region_3 = pd.read_pickle(os.path.join(BASE_DIR,"notebooks/no_outlier_3.pk1"))

    regions = {
        'benin-malanville': region_1, 'sierraleone-bumbuna': region_2, 'togo-dapang_qc': region_3
    }
    
    fig, axs = plt.subplots(1, 3, figsize=(18, 6))

    # Scatter plot for GHI vs. Tamb
    axs[0].scatter(regions[region]['GHI'], regions[region]['Tamb'], color='b')
    axs[0].set_title('GHI vs. Tamb')
    axs[0].set_xlabel('GHI')
    axs[0].set_ylabel('Tamb')
    axs[0].grid(True)

    # Scatter plot for WS vs. WSgust
    axs[1].scatter(regions[region]['WS'], regions[region]['WSgust'], color='r')
    axs[1].set_title('WS vs. WSgust')
    axs[1].set_xlabel('WS')
    axs[1].set_ylabel('WSgust')
    axs[1].grid(True)

    # Scatter plot for DNI vs. DHI
    axs[2].scatter(regions[region]['DNI'], regions[region]['DHI'], color='g')
    axs[2].set_title('DNI vs. DHI')
    axs[2].set_xlabel('DNI')
    axs[2].set_ylabel('DHI')
    axs[2].grid(True)

    # Adjust layout
    plt.tight_layout()
    return plt