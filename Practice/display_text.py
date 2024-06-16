#Core packages
import streamlit as st

# Additional package

#functions
def main():
    '''All code goes here'''
    st.title('Welcome to streamlit')



## Working with text
st.text("Hello World")
st.text("This is another text")
name = 'Arvind'
st.text(f"Welcome {name}")

# Header
st.header('This is header')

# subheader
st.subheader("This is subheader")

# Title
st.title("This is title")

# Markdow
st.markdown("## This is markdown")

## Colorful Text /Bootstrap alert
st.success("Succesfull")
st.warning("This is warning")
st.info('This is info')
st.error('This is an error')
st.exception('This is an exception')

## Superfunction

st.write("This is Normal text")
st.write('## This is markdown text')
st.write(1+2)
st.write(dir(st))

# Help info
st.help(range)