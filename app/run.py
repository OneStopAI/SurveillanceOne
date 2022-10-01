import streamlit as st
import tempfile


st.title("Surveillance One")


uploaded_file = st.file_uploader("Choose a video")

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(suffix='.mp4') as tmp_shp:
        tmp_shp.write(uploaded_file.read())
        st.video(tmp_shp.name)
