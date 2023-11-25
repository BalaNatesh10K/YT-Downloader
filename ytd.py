import streamlit as st
from pytube import YouTube
import os

downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')

st.title("YouTube Downloader")
st.subheader("Enter video URL:")

url = st.text_input(label='URL')

if url != '':
    yt = YouTube(url)
    st.image(yt.thumbnail_url)
    st.subheader('''
    {}
    ## Length: {} seconds
    ## Rating: {}
    '''.format(yt.title, yt.length, yt.rating))
    video = yt.streams

    if len(video) > 0:
        downloaded, download_audio = False, False
        download_video = st.button("Download Video")

        if yt.streams.filter(only_audio=True):
            download_audio = st.button("Download Audio Only")
        if download_video:
            video.get_highest_resolution().download(downloads_path)
            downloaded = True
        # if download_audio:
        #     video.filter(only_audio=True).first().download(downloads_path)
        #     downloaded = True
        if downloaded:
            st.subheader("Download Complete")
    else:
        st.subheader("This video can't be downloaded")
