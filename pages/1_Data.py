import streamlit as st
from streamlit_agraph import agraph
import pandas as pd
from modules.component import data_file_selector, info_sidebar, data_sidebar
from modules.utils import middle_element
from modules.llm import data_description_generation

# initialize session state
session_state_keys = ['data_file', 'data_description']
for key in session_state_keys:
    if key not in st.session_state:
        st.session_state[key] = None

st.set_page_config(
    page_title="Data",
    page_icon="👋",
    layout="wide"
)
st.title('Data Exploration')
info_sidebar()
data_sidebar()

# select data file
data_file_selector()

if st.session_state.get("data_file"):
    st.subheader("Data Details")
    for name, df in st.session_state.data_file.items():
        with st.expander(f"{name}", expanded=True):
            st.dataframe(df.head(10),  use_container_width=True)
            st.dataframe(df.describe(),  use_container_width=True)

    st.subheader("Data Description")
    st.info('You can either generate a description of the data items with LLM or you can simply modify in the table.', icon="ℹ️")
    for name, df in st.session_state.data_file.items():
        with st.expander(f"{name}", expanded=True):
            desc_df = st.session_state.data_description[name]
            col3 = middle_element([3,3,1], 3)
            with col3:
                if st.button("Generate Description", key=f"gd_{name}", use_container_width=True, type='primary'):
                    data_description_generation(desc_df)
            st.data_editor(desc_df, use_container_width=True)
    
    st.subheader("Relation Visualization")
    
    # st.markdown("##### Download & Fill the template then Upload.")
    col0, col1, col2 = st.columns([2, 3, 1])
    with col0:
        st.info('Upload relation file to generate relation graph. Generate with LLM if no file uploaded.', icon="ℹ️")
    with col1:
        uploaded_files = st.file_uploader("Choose a file", label_visibility='collapsed', type=['csv'], accept_multiple_files=True)
    with col2:
        if st.button("Download Template", use_container_width=True, type='primary'):
            pass
        if st.button("Generate Relation", use_container_width=True, type='primary'):
            pass

    for uploaded_file in uploaded_files:
        pass
