import streamlit as st
import os
import pandas as pd
from . import project

def data_sidebar():
    if not st.session_state.project:
        st.sidebar.error("No project selected, Please select a project in Welcome page.")
        return
    project_path = st.session_state.project + '\\data\\'
    data_csv = {name:os.path.join(project_path, name) for name in os.listdir(project_path) if os.path.join(project_path, name).endswith(".csv")}
    names = list(data_csv.keys())
    st.sidebar.subheader("Current Project: {}".format(st.session_state.project.split('\\')[-1]))
    name = st.sidebar.selectbox(
        "Select a data file:",
        names,
        label_visibility='collapsed',
        index=None,
    )
    if st.sidebar.button("Load Data", use_container_width=True, type='primary') and name:
        progress_text = "Loading Data..."
        my_bar = st.sidebar.progress(0, text=progress_text)
        chunk_size, chunk_list = 1, []
        total_lines = sum(1 for line in open(data_csv[name], encoding='utf-8')) - 1
        for chunk in pd.read_csv(data_csv[name], chunksize=chunk_size, encoding='utf-8'):
            chunk_list.append(chunk)
            my_bar.progress(len(chunk_list)/total_lines, text=progress_text)
        my_bar.empty()
        st.session_state.data_file = pd.concat(chunk_list, axis=0)
        st.session_state.data_file_name = name
            
def project_sidebar():
    st.sidebar.title("Projects")
    projects = project.get_project_dict()
    names = list(projects.keys())
    name = st.sidebar.selectbox(
        "Select a project:",
        names
    )
    if st.sidebar.button("Load"):
        st.session_state.project = projects[name]
        