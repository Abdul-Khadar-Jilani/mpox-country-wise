import json
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the updated dataset
data = pd.read_excel('Data.xlsx')

# Preview the data
st.write("### Total Monkeypox Cases by Country")
st.write(data)

import streamlit as st
import json
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.globals import ChartType, SymbolType

# Load your data
# Assuming you have a dataframe `data` with 'Countries' and 'Cases' columns

# Initialize the Map
c = Map(init_opts=opts.InitOpts(bg_color="white"))
c.add("Monkeypox Cases", [list(z) for z in zip(data['Countries'], data['Cases'])], "world")
c.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
c.set_global_opts(
    title_opts=opts.TitleOpts(title="Monkeypox Cases by Country"),
    visualmap_opts=opts.VisualMapOpts(max_=data['Cases'].max()),
)

# Render the map to HTML
map_html = c.render_embed()

# Display in Streamlit using st.components.v1.html
st.components.v1.html(map_html, height=500)

# Filters for Countries (Main Page)
st.header('Filter Data')
countries = st.multiselect('Select Countries', options=data['Countries'].unique(), default=data['Countries'].unique())

# Filter the data based on selected countries
filtered_data = data[data['Countries'].isin(countries)]

# Visualization Selection on Main Page
st.header('Choose Visualization')
chart_type = st.selectbox('Select Chart Type', ['Bar Chart', 'Area Chart', 'Pie Chart', 'Line Chart', 'Scatter Plot', 'Heatmap'])

# Generate Plots based on selected chart type
st.write(f"### {chart_type} of Cases")

if chart_type == 'Bar Chart':
    st.bar_chart(filtered_data.set_index('Countries')['Cases'])

elif chart_type == 'Area Chart':
    st.area_chart(filtered_data.set_index('Countries')['Cases'])

elif chart_type == 'Pie Chart':
    fig, ax = plt.subplots()
    ax.pie(filtered_data.set_index('Countries')['Cases'], labels=filtered_data['Countries'], autopct='%1.1f%%')
    st.pyplot(fig)

elif chart_type == 'Line Chart':
    st.line_chart(filtered_data.set_index('Countries')['Cases'])

elif chart_type == 'Scatter Plot':
    fig, ax = plt.subplots()
    ax.scatter(filtered_data['Countries'], filtered_data['Cases'])
    ax.set_xlabel('Countries')
    ax.set_ylabel('Cases')
    plt.xticks(rotation=90)
    st.pyplot(fig)

elif chart_type == 'Heatmap':
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(filtered_data[['Cases']].T, cmap='coolwarm', annot=True, linewidths=.5, ax=ax)
    plt.xticks(rotation=45, ha='right')
    plt.yticks(rotation=0)
    ax.set_title('Heatmap of Monkeypox Cases by Country')
    st.pyplot(fig)



