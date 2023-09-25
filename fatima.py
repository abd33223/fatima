import pandas as pd
import streamlit as st
import plotly.express as px

# Load the dataset
df = pd.read_csv("Largest_Companies.csv")

# Add filters on the left side of the page
st.sidebar.header("Filters")

# Create a dictionary to store the filter options for each column
filter_options = {}

# Add all columns to the filter options
for column in df.columns:
    if column in ["Revenue (USD millions)", "Revenue growth", "Employees"]:
        # Add sliders for specific columns
        min_value = df[column].min()
        max_value = df[column].max()
        filter_options[column] = st.sidebar.slider(f"Select a value for {column}", min_value, max_value, (min_value, max_value))
    else:
        # Add selectboxes for other columns
        filter_options[column] = st.sidebar.selectbox(f"Select a {column}", df[column].unique())

# Apply filters to the DataFrame
filtered_df = df
for column, selected_value in filter_options.items():
    if column in ["Revenue (USD millions)", "Revenue growth", "Employees"]:
        # Filter based on slider values for specific columns
        min_value, max_value = selected_value
        filtered_df = filtered_df[(filtered_df[column] >= min_value) & (filtered_df[column] <= max_value)]
    else:
        # Filter based on selectbox values for other columns
        filtered_df = filtered_df[filtered_df[column] == selected_value]

# Visualization 1: Bargraph of Top 10 Companies with Highest Revenues
st.header("Visualization 1: Top 10 Companies with Highest Revenues")
top_10_revenue = filtered_df.sort_values(by='Revenue (USD millions)', ascending=False).head(10)
figure_1 = px.bar(top_10_revenue, x='Name', y='Revenue (USD millions)', title='Top 10 Companies with Highest Revenues')
st.plotly_chart(figure_1)

# Visualization 2: Scatter Plot of Revenue vs. Number of Employees
st.header("Visualization 2: Revenue vs. Number of Employees")
figure_2 = px.scatter(filtered_df, x='Revenue (USD millions)', y='Employees',
                  title='Revenue vs. Number of Employees',
                  labels={'Revenue (USD millions)': 'Revenue in USD (Millions)', 'Employees': 'Number of Employees'})
st.plotly_chart(figure_2)

# Visualization 3: Bar Chart of Distribution of Companies by a Selected Column
st.header("Visualization 3: Distribution of Companies by a Selected Column")
selected_column = st.sidebar.selectbox("Select a Column", df.columns)
column_distribution = filtered_df[selected_column].value_counts().reset_index()
column_distribution.columns = [selected_column, 'Count']
figure_3 = px.bar(column_distribution, x=selected_column, y='Count',
              title=f'Distribution of Companies by {selected_column}')
st.plotly_chart(figure_3)

# Visualization 4: Barplot of Distribution of Revenue Growth
st.header("Visualization 4: Distribution of Revenue Growth")
figure_4 = px.box(filtered_df, y='Revenue growth', title='Distribution of Revenue Growth')
st.plotly_chart(figure_4)
