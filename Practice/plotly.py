import streamlit as st

#laod EDA packages
import pandas as pd
import numpy as np

# Loda Data visualization packages
import plotly.express as px


def main():
    st.title("Plotting In streamlit with plotly")

    df = pd.read_csv("data/prog_languages_data.csv")
    st.dataframe(df)

    fig = px.pie(df,values='Sum',names='lang',title='Pie Chart of Languages')
    st.plotly_chart(fig)

    fig1 = px.bar(df,x='lang',y='Sum')
    st.plotly_chart(fig1)

if __name__ == '__main__':
    main()