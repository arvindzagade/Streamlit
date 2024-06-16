# library imports
import streamlit as st

# Select/Multiple select

my_lang = ['Python','C','Java','Julia']

choice = st.selectbox("Language",my_lang)
st.write(f"You have selected {choice}")

## Multiple selection
spoken_lang = ("English","Hindi","Marathi","German")
my_spoken_lang = st.multiselect("Spoken Lang",spoken_lang,default='English')


# Slider
## Numbers (Int/Float/Date)
age = st.slider("Age",1,100)

# Any other datatype
# Select slider
color = st.select_slider("Choose Color",options=["yellow",'red','blue','white','green'],value=("yellow","red"))