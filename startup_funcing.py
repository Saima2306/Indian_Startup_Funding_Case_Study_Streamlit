import streamlit as st
import pandas as pd
import datetime
data = pd.read_csv('./startup_clean.csv')
data['Date'] = pd.to_datetime(data['Date'],errors='coerce')
data['Year'] = data['Date'].dt.year
data['Month'] = data['Date'].dt.month
import matplotlib.pyplot as plt
st.set_page_config(layout="wide",page_title="Startup Analysis")
def load_overall_analysis():
    st.title('Overall Analysis')
    total = round(data['amount1'].sum())
    max_funding = round(data.groupby('Startup')['amount1'].max().sort_values(ascending = False).head(1).values[0])
    avg_funding = round(data.groupby('Startup')['amount1'].sum().mean())
    total_funded_startup = data[~(data['amount1'] == 0)]['Startup'].count()
    col1,col2,col3,col4 = st.columns(4)
    with col1:
        st.metric('Total',str(total)+' Cr')
    with col2:
        st.metric('Maximum Funding',str(max_funding)+' Cr')
    with col3:
        st.metric('Average Funding', str(avg_funding) + ' Cr')
    with col4:
        st.metric('Total Funded startup', str(total_funded_startup) + ' Cr')
    st.subheader('MoM investment graph')
    selected_option = st.selectbox('Select type',['Total','Count'])
    if selected_option == 'Total':
        temp_df = data.groupby(['Year', 'Month'])['amount1'].sum().reset_index()
        temp_df['X_axis'] = temp_df['Year'].astype(str) + '-' + temp_df['Month'].astype(str)
        fig3, ax = plt.subplots()
        ax.plot(temp_df['X_axis'], temp_df.amount1.values)
        st.pyplot(fig3)
    elif selected_option == 'Count':
        temp_df = data.groupby(['Year', 'Month'])['Startup'].count().reset_index()
        temp_df['X_axis'] = temp_df['Year'].astype(str) + '-' +temp_df['Month'].astype(str)
        fig3, ax = plt.subplots()
        ax.plot(temp_df['X_axis'], temp_df.Startup.values)
        st.pyplot(fig3)

def load_investor_details(investor):
    st.title(investor)
    # load the recent 5 invstment
    last5_df = data[data['investors'].str.contains(investor)].head()[['Date', 'Startup', 'Vertical', 'City', 'round', 'amount1']]
    st.subheader('Most recent investments')
    st.dataframe(last5_df)
    #Biggest investments
    col1,col2 = st.columns(2)
    with col1:
        big_df = data[data['investors'].str.contains(investor)].groupby('Startup')['amount1'].sum().sort_values(ascending = False).head()
        st.subheader('Most biggest achievement')
        fig, ax = plt.subplots()
        ax.bar(big_df.index,big_df.values)
        st.pyplot(fig)
    with col2:
        vertical_df = data[data['investors'].str.contains(investor)].groupby('Vertical')['amount1'].sum()
        fig, ax = plt.subplots()
        st.subheader('Sector invested in')
        ax.pie(vertical_df,labels=vertical_df.index,autopct = "%0.01f%%")
        st.pyplot(fig)
    data['Year'] = data['Date'].dt.year
    yoy_df = data[data['investors'].str.contains(investor)].groupby('Year')['amount1'].sum()
    st.subheader('YoY investment graph')
    fig, ax = plt.subplots()
    ax.plot(yoy_df.index, yoy_df.values)
    st.pyplot(fig)
st.sidebar.title('Startup Funding Analysis')
option = st.sidebar.selectbox('Select one',['Overall Analysis','Startup','Investor'])
if option == 'Overall Analysis':
    # btn0 = st.sidebar.button('Show overall analysis')
    # if btn0:
    load_overall_analysis()

elif option == 'Startup':
    st.sidebar.selectbox('Select Startup',sorted(data['Startup'].unique().tolist()))
    btn1 = st.sidebar.button('Find Startup details')
    st.title('Startup Analysis')
else:
    investor_name = st.sidebar.selectbox('Select Investor',sorted(set(data['investors'].str.split(',').sum())))
    btn2 = st.sidebar.button('find investor details')
    if btn2:
        load_investor_details(investor_name)