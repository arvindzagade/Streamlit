import streamlit as st

# Text Input
fname = st.text_input('Enter firstname',max_chars=10)
# Text Input Hide Password
password = st.text_input("Enter Password",type='password')
st.title(fname)

# text area
message = st.text_area("Enter message",height=100)
st.write(message)

# Numbers
number = st.number_input("Enter number",1.0,25.0)

# Date Input
myappointment = st.date_input("Appointment")

# Time Input
mytime = st.time_input("My time")

# color Picker
color = st.color_picker("Select Color")
