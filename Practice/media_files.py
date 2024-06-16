# library imports
import streamlit as st

## Working Media files (video/images/audio)
#Display Images

from PIL import Image
img = Image.open("data/image_01.jpg")
st.image(img,use_column_width=True)


# From Url
st.image('https://alcorfund.com/wp-content/uploads/2020/09/Technical-Innovation.png')

## Display Videos

# video_file = open("data/secret_of_success.mp4",'rb').read()
# st.video(video_file,start_time=3)

# Display Audion files
audio_file = open("data/song.mp3","rb")
st.audio(audio_file.read(),format='audio/mp3')
