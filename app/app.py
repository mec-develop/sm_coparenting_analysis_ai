import streamlit as st
import os
from supabase_client import supabase


def save_file(uploaded_file):
    upload_dir = "uploads"
    os.makedirs(upload_dir, exist_ok=True)
    file_path = os.path.join(upload_dir, uploaded_file.name)

    if os.path.exists(file_path):
        return False, file_path

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return True, file_path


st.set_page_config(page_title="Life Snippet Engine")

st.sidebar.title("Navigation")
if "active_analysis" not in st.session_state:
    st.session_state.active_analysis = "Video Analysis"


def set_video_active():
    st.session_state.active_analysis = "Video Analysis"


def set_text_active():
    st.session_state.active_analysis = "Text Analysis"


with st.sidebar.expander("Video Analysis", expanded=True):
    video_page = st.radio(
        "Video Analysis Pages",
        ["Reports", "Ingest"],
        key="video_page",
        on_change=set_video_active,
    )

with st.sidebar.expander("Text Analysis", expanded=True):
    text_page = st.radio(
        "Text Analysis Pages",
        ["Reports", "Ingest"],
        key="text_page",
        on_change=set_text_active,
    )

active_analysis = st.session_state.active_analysis
selected_page = video_page if active_analysis == "Video Analysis" else text_page

if active_analysis == "Video Analysis" and selected_page == "Reports":
    st.header("Video Reports")
    st.write("Reports will appear here")
elif active_analysis == "Video Analysis" and selected_page == "Ingest":
    st.header("Ingest Videos")
    try:
        if supabase:
            st.success("Supabase connected")
    except Exception as e:
        st.error("Supabase connection failed")
    st.write("Upload and process videos")
    uploaded_files = st.file_uploader(
        "Upload video files",
        type=["mov", "mp4"],
        accept_multiple_files=True,
    )
    if uploaded_files:
        for uploaded_file in uploaded_files:
            saved, file_path = save_file(uploaded_file)
            if not saved:
                st.warning(f"File already exists: {uploaded_file.name}")
            else:
                st.success(f"Saved {uploaded_file.name}")

        import os
        upload_dir = "uploads"
        os.makedirs(upload_dir, exist_ok=True)
        files = sorted(os.listdir(upload_dir))
        st.write("Files in uploads:")
        for file_name in files:
            st.write(f"- {file_name}")
    st.subheader("Processing Status")
    upload_dir = "uploads"
    files = []

    if os.path.exists(upload_dir):
        files = os.listdir(upload_dir)

    status_rows = [
        {
            "File Name": file_name,
            "Audio": "Pending",
            "Transcript": "Pending",
            "Scored": "Pending",
            "Ready": "Pending",
        }
        for file_name in files
    ]
    st.table(status_rows)
elif active_analysis == "Text Analysis" and selected_page == "Reports":
    st.header("Text Reports")
    st.write("Reports will appear here")
elif active_analysis == "Text Analysis" and selected_page == "Ingest":
    st.header("Ingest Text Data")
    st.write("Placeholder content for text analysis.")
