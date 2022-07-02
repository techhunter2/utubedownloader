import streamlit as st
from pytube import YouTube
st.title('Youtube Video Downloader')
with st.form("form"):
    link=st.text_input("Paste the link")
    s_state1=st.form_submit_button("Enter")
    if s_state1:
        if link == "":
            st.warning("Please paste link")
        else:
            yt = YouTube(link)
            url=yt.thumbnail_url
            st.image(url,width=650)
            st.write(yt.title,yt.views)
            st.title('Descriptions')
            st.write(yt.description)
option = st.selectbox(
'Select type of download',
('Audio', '3gp', '720p'))
matches = ['audio', '3gp', '720p']
if st.button("download"): 
    video_object =  YouTube(link)
    if option=='Audio':
        video_object.streams.get_audio_only().download() 		
    elif option=='3gp':
        video_object.streams.get_lowest_resolution().download()
    elif option=='720p':
        video_object.streams.get_highest_resolution().download()
            
