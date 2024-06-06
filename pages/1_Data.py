import streamlit as st
st.set_page_config(
    page_title="Data",
    page_icon="👋",
    layout="wide"
)

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

st.title('Data Exploration')
info_sidebar()
data_sidebar()

# select data file
data_file_selector()
st.divider()
if st.session_state.get("data_file"):
    st.subheader("Data Details")
    for name, df in st.session_state.data_file.items():
        with st.expander(f"{name}", expanded=True):
            st.dataframe(df.head(10),  use_container_width=True)
            st.dataframe(df.describe(),  use_container_width=True)
    st.divider()
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
    st.divider()
    st.subheader("Relation Visualization")
    from modules.utils import NODE_RELATIONSHIP_TEMPLATE, EDGE_RELATIONSHIP_TEMPLATE
    st.error("Sorry, this feature is not available yet.", icon="🥹")
    st.info('Upload relation file to generate relation graph. Generate with LLM if no file uploaded.', icon="ℹ️")
    col0, col1, col2, col3 = st.columns([4, 1, 1, 1])
    with col0:
        uploaded_files = st.file_uploader("Choose a file", label_visibility='collapsed', type=['csv'], accept_multiple_files=True)
    with col1:
       st.download_button(label="Download Node Template", data=NODE_RELATIONSHIP_TEMPLATE, file_name="data_relationship_node_template.csv", mime="text/csv", type='primary')
    with col2:
        st.download_button(label="Download Edge Template", data=EDGE_RELATIONSHIP_TEMPLATE, file_name="data_relationship_edge_template.csv", mime="text/csv", type='primary')
    with col3:
        if st.button("Generate Relation Graph", use_container_width=True, type='primary'):
            st.toast("This feature is not available yet.", icon="🥹")
    st.divider()
    st.subheader("Generate Scenarios")
    # TODO: data item multi-selectors
    # TODO: generate prompt button
    # TODO: info to hint the modification
    # TODO: maybe some modules of the prompts?
    with st.expander("Prompt", expanded=False):
        st.text_area("temp", label_visibility='collapsed', height=300)
    col2 = middle_element([2,1,2])
    with col2:
        if st.button("Generate Scenarios", use_container_width=True, type='primary'):
            st.toast("This feature is not available yet.", icon="🥹")