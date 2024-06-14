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
        st.error("No project selected. Please select a project first.", icon="🚫")
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
        st.session_state.scenario_tree.data = st.session_state.data_file
    st.divider()

## Scenario Page components
def scenario_selector(tree):
    col1, col2, col3 = st.columns([3,3,1])
    with col1:
        st.write("Select a branch:")
    with col2:
        st.write("Select a scenario:")
    col1, col2, col3 = st.columns([3,3,1])

    with col1:
        sp_current_branch = st.selectbox("Branch", list(tree.branches.keys()), label_visibility='collapsed')
    with col2:
        sp_current_scenario = st.selectbox("Scenario", [s.id for s in tree.get_branch(sp_current_branch).scenarios], label_visibility='collapsed')
    with col3:
        if st.button("Confirm", type='primary', use_container_width=True):
            st.session_state.current_scenario = tree.get_branch(sp_current_branch).get_scenario_by_id(sp_current_scenario)

def scenario_data():
    for k, v in st.session_state.selected_items_dict.items():
        cols = [i['name'] for i in v]
        df = st.session_state.data_description[k]
        selected_df = df.loc[df['name'].isin(cols)]
        with st.expander(k, expanded=False):
            st.data_editor(selected_df, use_container_width=True)