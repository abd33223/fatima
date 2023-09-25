import pandas as pd
import streamlit as st
import plotly.express as px

# Load the dataset
df = pd.read_csv("Largest_Companies.csv")

# Add filters on the left side of the page
st.sidebar.header("Filters")

# Filter by Industry
selected_industry = st.sidebar.selectbox("Select an Industry", df['Industry'].unique())

# Filter by Country
selected_country = st.sidebar.selectbox("Select a Country", df['Country'].unique())

# Apply filters to the DataFrame
filtered_df = df[(df['Industry'] == selected_industry) & (df['Country'] == selected_country)]

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

# Visualization 3: Bar Chart of Distribution of Companies by Country
st.header("Visualization 3: Distribution of Companies by Country")
country_distribution = filtered_df['Country'].value_counts().reset_index()
country_distribution.columns = ['Country', 'Count']
figure_3 = px.bar(country_distribution, x='Country', y='Count',
              title='Distribution of Companies by Country')
st.plotly_chart(figure_3)

# Visualization 4: Barplot of Distribution of Revenue Growth
st.header("Visualization 4: Distribution of Revenue Growth")
figure_4 = px.box(filtered_df, y='Revenue growth', title='Distribution of Revenue Growth')
st.plotly_chart(figure_4)
