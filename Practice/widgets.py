## library imports
import streamlit as st

# working with widgets
# Buttons/Radio/Checkbox/Select

#Working with Buttons
name = 'Arvind'

if st.button('Submit'):
    st.write(f'Name: {name.upper()}')

# if we have two buttons with same name we can pass key
if st.button('Submit',key='newsubmit'):
    st.write(f'Last Name: {name.lower()}')


# Working with RadioButtons
status = st.radio("What is your status",("Active","Inactive"))
if status == 'Active':
    st.success("You are Active")
elif status == "Inactive":
    st.warning('Inactive')

# Working with Checkbox
if st.checkbox("Show/Hide"):
    st.text("showing Something")

# Working with Beta expander
if st.expander('Python'):
    st.success("Hello Python")

with st.expander('Julia'):
    st.text("Hello Julia")