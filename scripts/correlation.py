import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def correlation(region):

    region_1 = pd.read_pickle(os.path.join(BASE_DIR,"notebooks/no_outlier_1.pk1"))

    region_2 = pd.read_pickle(os.path.join(BASE_DIR,"notebooks/no_outlier_2.pk1"))

    region_3 = pd.read_pickle(os.path.join(BASE_DIR,"notebooks/no_outlier_3.pk1"))

    regions = {
        'benin-malanville': region_1, 'sierraleone-bumbuna': region_2, 'togo-dapang_qc': region_3
    }

    selected_columns = ['GHI', 'DNI', 'DHI', 'TModA', 'TModB']
    df_selected_1 = regions[region][selected_columns]

    correlation_matrix = df_selected_1.corr()


    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, linewidths=.5)
    plt.title('Correlation Matrix (GHI, DHI, DNI vs TModA)')
    return plt
