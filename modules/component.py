import streamlit as st
import os
import pandas as pd
from modules.utils import NODE_RELATIONSHIP_TEMPLATE, EDGE_RELATIONSHIP_TEMPLATE

## Sidebar components
def info_sidebar():
    if st.session_state.get('project'):
        st.sidebar.success("Project '{}' loaded successfully!".format(st.session_state.project.split('\\')[-1]))
    else:
        st.sidebar.error("No project selected.")
        
    if st.session_state.get('llm'):
        st.sidebar.success("LLM has been set up successfully!")
    else:
        st.sidebar.warning("LLM unavailable. Check your settings.")
        
def data_sidebar():
    if st.session_state.get('project'):
        if st.session_state.get('data_file'):
            st.sidebar.success("Data loaded successfully!")
        else:
            st.sidebar.warning("No data loaded yet.")

## Data Page components
def data_file_selector():
    if not st.session_state.get('project'):
        return
    project_path = st.session_state.project + '\\data\\'
    data_csv = {name:os.path.join(project_path, name) for name in os.listdir(project_path) if os.path.join(project_path, name).endswith(".csv")}
    names = list(data_csv.keys())
    st.subheader("Select data file(s)")
    col1, col2 = st.columns([7, 1])
    with col1:
        name = st.multiselect(
            "Select data files:",
            names,
            label_visibility='collapsed'
        )
    with col2:
        confirm_button = st.button("Confirm", use_container_width=True, type='primary')
    if confirm_button and name:
        st.session_state.data_file = {}
        st.session_state.data_description = {}
        progress_text = "Loading Data..."
        for n in name:
            my_bar = st.progress(0, text=progress_text)
            chunk_size, chunk_list = 1, []
            total_lines = sum(1 for line in open(data_csv[n], encoding='utf-8')) - 1
            for chunk in pd.read_csv(data_csv[n], chunksize=chunk_size, encoding='utf-8'):
                chunk_list.append(chunk)
                my_bar.progress(len(chunk_list)/total_lines, text=progress_text)
            my_bar.empty()
            df = pd.concat(chunk_list)
            st.session_state.data_file[n] = df
            st.session_state.data_description[n] = pd.DataFrame({'name': df.columns, 'type': [str(t) for t in df.dtypes.tolist()], 'description': [''] * len(df.columns), 'example': [df.iloc[0,i] for i in range(len(df.columns))]}, index=range(1, len(df.columns) + 1))


