import streamlit as st

st.set_page_config(page_title="Life Snippet Engine")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Video Analysis", "Text Analysis"])

if page == "Video Analysis":
    st.header("Video Analysis")
    st.write("Placeholder content for video analysis.")
elif page == "Text Analysis":
    st.header("Text Analysis")
    st.write("Placeholder content for text analysis.")
