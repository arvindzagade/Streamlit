## library imports
import streamlit as st

## loading data
import pandas as pd

# Displaying data
df = pd.read_csv('data\iris.csv')

# Method1
st.dataframe(df)

#Adding a color style from pandas
st.dataframe(df.style.highlight_max(axis=0))

# Method 2: static table
#st.table(df)

# Method 3: Using superfunction
st.write(df.head())

# Display Json
st.json({'data':'Name'})

#Displaying code
mycode = """
def sayhello():
    print("Hello")
end
"""

st.code(mycode,language='python')