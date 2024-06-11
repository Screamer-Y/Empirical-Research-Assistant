import streamlit as st
st.set_page_config(
    page_title="Data",
    page_icon="👋",
    layout="wide"
)

from streamlit_agraph import agraph
import pandas as pd
from modules.component import data_file_selector, info_sidebar, data_sidebar
from modules.utils import middle_element, get_selected_items_dict
from modules.llm import data_description_generation, data_relationship_generation
from modules.prompt import *
import json, time
from hashlib import md5

# initialize session state
session_state_keys = ['data_file', 'data_description', 'scenario_output']
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
            col3 = middle_element([3,2,1], 3)
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
    items_option = [f"{name}: {col}" for name, df in st.session_state.data_file.items() for col in df.columns]
    selected_items = st.multiselect("Select Data Items", items_option, default=None, placeholder="Select Data Items", label_visibility='collapsed')
    selected_items_dict = get_selected_items_dict(selected_items)
    st.info("You can modify the prompt below, add requirements in the <User Guidance>, and generate scenarios.", icon="ℹ️")
    with st.expander("##Prompt##", expanded=False):
        system_prompt = st.text_area("System Prompt", value=GENERATE_SCENARIO_SYSTEM_PROMPT,height=150)
        human_input = st.text_area("Human Input", value=f"<User Input>\n{json.dumps(selected_items_dict, ensure_ascii=False, indent=4)}", height=150)
        user_guidance = st.text_area("User Guidance", value="<User Guidance>\n")
    col2 = middle_element([2,1,2])
    with col2:
        if st.button("Generate Scenarios", use_container_width=True, type='primary'):
            # in json format
            scenario = data_relationship_generation(system_prompt, human_input, user_guidance)
            st.session_state.scenario_output = json.loads(scenario)
    st.divider()
    if st.session_state.get("scenario_output"):    
        with st.expander("Scenario", expanded=True):
            scenario_str = ''
            for key, value in st.session_state.scenario_output.items():
                # st.markdown(f"### {key}\n{value}\n")
                scenario_str += f"### {key}\n{value}\n"
            scenario_str = scenario_str[:-1]
            st.markdown(scenario_str)
            if st.button("Save Scenarios", type='primary'):
                branch_id = md5(''.join(selected_items).encode()).hexdigest()
                st.session_state.scenario_tree.add_scenario(branch_id, st.session_state.scenario_output['Scenario Name'], scenario_str)
                st.success("Scenarios saved successfully!")
      
    
            