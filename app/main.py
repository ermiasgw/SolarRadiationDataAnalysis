import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os,sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from scripts import scatter_plots, histogram, temprature, wind, correlation, time_series

# Title of the dashboard
st.title('Solar Radiation Data Analysis Dashboard')

region = st.sidebar.selectbox('Select Region', ['benin-malanville', 'sierraleone-bumbuna', 'togo-dapang_qc'])

# Menu to select scatter plot
chart_type = st.sidebar.selectbox('Select Chart Type', ['Scatter Plot', 'Histogram', 'Temperature Analysis', 'Wind Analysis', 'Correlation Analysis', 'Time Series Analysis'])


# Scatter plot section
if chart_type == 'Scatter Plot':
    st.subheader('Scatter Plots')
    st.pyplot(scatter_plots.scatter(region))
    
    

# Histogram section
elif chart_type == 'Histogram':
    st.subheader('Histograms')
    st.pyplot(histogram.histogram(region))

# Temperature Analysis section
elif chart_type == 'Temperature Analysis':
    st.subheader('Temperature Analysis')
    st.pyplot(temprature.temprature(region))

# Wind Analysis section
elif chart_type == 'Wind Analysis':
    st.subheader('Wind Analysis')
    st.pyplot(wind.wind(region))

# Correlation Analysis section
elif chart_type == 'Correlation Analysis':
    st.subheader('Correlation Analysis')
    st.pyplot(correlation.correlation(region))

# Time Series Analysis section
elif chart_type == 'Time Series Analysis':
    st.subheader('Time Series Analysis')
    st.pyplot(time_series.time_series(region))


    