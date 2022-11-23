import pandas as pd
from os import chdir
from matplotlib import pyplot as plt
import seaborn as sns
import streamlit as st
import numpy as np

st.set_page_config(layout='wide')

# ---------------------------------------SIDEBAR PORTION START---------------------------------------- # 
fig_width = st.sidebar.slider(
    'Width of the figure',
    min_value=8.0, max_value=20.0, step=0.5, value=15.0
)
fig_height = st.sidebar.slider(
    'Height of the figure',
    min_value=5.0, max_value=10.0, step=0.5
)
# ----------------------------------------SIDEBAR PORTION END----------------------------------------- #

with open('URL_column_names.txt', 'r') as file:
    columns = file.readlines()
    columns = [value.rstrip() for value in columns]
    
columns.sort()

with open('palette_values.txt', 'r') as file:
    palette_values = file.readlines()
    palette_values = [palette_name.rstrip() for palette_name in palette_values]

st.title("Malicious URL dataset visualisation")
st.markdown("""
    Use this page to visualise the extracted features of the malicious URL dataset.
""")

df = pd.read_csv('URL_dataset_ready.csv')

st.write(df.head())

# Choose the variable for the x-axis.
selected_x = st.selectbox(
    'Choose the variable for the x-axis',
    columns
)

# BOXPLOT
st.markdown("# Box plot")
log_scale = st.selectbox(
    'Which scale would you like to use for the boxplot?',
    ['linear', 'symlog', 'log']
)

fig, ax = plt.subplots(figsize=(fig_width, fig_height))
sns.set(font_scale=1)
ax = sns.boxplot(
    data=df,
    x=selected_x,
    y='type',
    orient='h',
    palette=np.random.choice(palette_values)
)
ax.set_xscale(log_scale)
plt.title(f'{selected_x} VS URL type')
plt.tight_layout()
plt.grid()
st.pyplot(fig)


# Histrogram plot
st.markdown("Histogram plot")

bin_count = st.number_input(
    label='How many bins do you want?',
    min_value=5,
    max_value=100,
    value=10,
    step=1
)

hist_log_scale = st.selectbox(
    'Do you want to use a log scale for the histplot?',
    ['Yes', 'No']
)

fig, ax = plt.subplots(figsize=(fig_width, fig_height))
sns.set(font_scale=1)
ax = sns.histplot(
    data=df,
    x=selected_x,
    hue='type',
    palette=np.random.choice(palette_values),
    bins=bin_count,
    multiple='dodge',
    shrink=0.9
)
if hist_log_scale == 'Yes':
    ax.set_yscale("symlog")
else:
    ax.set_yscale('linear')
plt.title(f'{selected_x} VS URL type')
plt.tight_layout()
plt.grid()
st.pyplot(fig)