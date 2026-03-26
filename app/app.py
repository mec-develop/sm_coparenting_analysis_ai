import streamlit as st
from supabase_client import supabase

st.set_page_config(page_title="Life Snippet Engine")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Video Analysis", "Text Analysis"])

if page == "Video Analysis":
    st.header("Video Analysis")
    try:
        if supabase:
            st.success("Supabase connected")
    except Exception as e:
        st.error("Supabase connection failed")
    st.write("Placeholder content for video analysis.")
elif page == "Text Analysis":
    st.header("Text Analysis")
    st.write("Placeholder content for text analysis.")
