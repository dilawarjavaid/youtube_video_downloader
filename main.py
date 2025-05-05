import streamlit as st
from pytube import YouTube

#Set app title
st.title('YouTube Video Downloader')

#Create Input Field for YouTube URL
video_url = st.text_input('Enter the YouTube video URL')

