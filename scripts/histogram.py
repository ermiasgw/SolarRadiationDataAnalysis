import pandas as pd
import matplotlib.pyplot as plt
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def histogram(region):

    region_1 = pd.read_pickle(os.path.join(BASE_DIR,"notebooks/no_outlier_1.pk1"))

    region_2 = pd.read_pickle(os.path.join(BASE_DIR,"notebooks/no_outlier_2.pk1"))

    region_3 = pd.read_pickle(os.path.join(BASE_DIR,"notebooks/no_outlier_3.pk1"))

    regions = {
        'benin-malanville': region_1, 'sierraleone-bumbuna': region_2, 'togo-dapang_qc': region_3
    }
    
    # Create histograms for variables
    fig, axs = plt.subplots(3, 2, figsize=(14, 12))

    # Histogram for GHI
    axs[0, 0].hist(regions[region]['GHI'], bins=10, color='b', alpha=0.7)
    axs[0, 0].set_title('GHI Histogram')
    axs[0, 0].set_xlabel('GHI')
    axs[0, 0].set_ylabel('Frequency')

    # Histogram for DNI
    axs[0, 1].hist(regions[region]['DNI'], bins=10, color='r', alpha=0.7)
    axs[0, 1].set_title('DNI Histogram')
    axs[0, 1].set_xlabel('DNI')
    axs[0, 1].set_ylabel('Frequency')

    # Histogram for DHI
    axs[1, 0].hist(regions[region]['DHI'], bins=10, color='g', alpha=0.7)
    axs[1, 0].set_title('DHI Histogram')
    axs[1, 0].set_xlabel('DHI')
    axs[1, 0].set_ylabel('Frequency')

    # Histogram for WS
    axs[1, 1].hist(regions[region]['WS'], bins=10, color='orange', alpha=0.7)
    axs[1, 1].set_title('WS Histogram')
    axs[1, 1].set_xlabel('WS')
    axs[1, 1].set_ylabel('Frequency')

    # Histogram for Module Temperatures (TModA, TModB)
    axs[2, 0].hist(regions[region][['TModA', 'TModB']], bins=10, color=['purple', 'brown'], alpha=0.7, label=['TModA', 'TModB'])
    axs[2, 0].set_title('Module Temperatures Histogram')
    axs[2, 0].set_xlabel('Temperature (°C)')
    axs[2, 0].set_ylabel('Frequency')
    axs[2, 0].legend()

    # Histogram for Ambient Temperature (Tamb)
    axs[2, 1].hist(regions[region]['Tamb'], bins=10, color='gray', alpha=0.7)
    axs[2, 1].set_title('Ambient Temperature Histogram')
    axs[2, 1].set_xlabel('Tamb')
    axs[2, 1].set_ylabel('Frequency')

    # Adjust layout
    plt.tight_layout()

    return plt