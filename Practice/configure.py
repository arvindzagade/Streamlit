import streamlit as st
from PIL import Image
img = Image.open('data/image_03.jpg')
## Changing the Tab icon
#Must be the first activity
#st.set_page_config(page_title='Hello') # Before 0.70.0

# Method _1
# st.set_page_config(page_title='Hello',page_icon='🌍'
#                    ,layout='wide',initial_sidebar_state='auto')

# Method 2: Dictionary
PAGE_CONFIG = {'page_title':'streamlit','page_icon':":smiley:","layout":"centered"}
st.set_page_config(**PAGE_CONFIG)

# Function

def main():
    st.title("Welcome to streamlit ❤️🩷🧡💛💚💙🩵💜🖤🩶")
    st.sidebar.success("Menu")

if __name__ == '__main__':
    main()