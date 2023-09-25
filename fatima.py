import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

# Load the dataset
largest_companies = st.file_uploader("Upload CSV file", type=["csv"])

if largest_companies is not None:
    largest_companies = pd.read_csv(largest_companies)

    # Visualization 1: Bargraph of Top 10 Companies with Highest Revenues
    st.header("Visualization 1: Top 10 Companies with Highest Revenues")
    top_10_revenue = largest_companies.sort_values(by='Revenue (USD millions)', ascending=False).head(10)
    figure_1 = px.bar(top_10_revenue, x='Name', y='Revenue (USD millions)', title='Top 10 Companies with Highest Revenues')
    st.plotly_chart(figure_1)

    # Visualization 2: Scatter Plot of Revenue vs. Number of Employees
    st.header("Visualization 2: Revenue vs. Number of Employees")
    figure_2 = px.scatter(largest_companies, x='Revenue (USD millions)', y='Employees',
                      title='Revenue vs. Number of Employees',
                      labels={'Revenue (USD millions)': 'Revenue in USD (Millions)', 'Employees': 'Number of Employees'})
    st.plotly_chart(figure_2)

    # Visualization 3: Pie Chart of Distribution of Companies Over Industries
    st.header("Visualization 3: Distribution of Companies Over Industries")
    industry_distribution = largest_companies['Industry'].value_counts().reset_index()
    industry_distribution.columns = ['Industry', 'Count']
    figure_3 = px.pie(industry_distribution, names='Industry', values='Count',
                  title='Distribution of Companies Over Industries')
    st.plotly_chart(figure_3)

    # Visualization 4: Barplot of Distribution of Revenue Growth
    st.header("Visualization 4: Distribution of Revenue Growth")
    figure_4 = px.box(largest_companies, y='Revenue growth', title='Distribution of Revenue Growth')
    st.plotly_chart(figure_4)

    # Visualization 5: Treemap of Revenue Distribution by Industry
    st.header("Visualization 5: Revenue Distribution by Industry (Treemap)")
    figure_5 = px.treemap(largest_companies,
                      path=['Industry', 'Name'],
                      values='Revenue (USD millions)',
                      title='Revenue Distribution by Industry (Treemap)')

    st.plotly_chart(figure_5)
