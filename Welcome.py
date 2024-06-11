import streamlit as st
st.set_page_config(
    page_title="Welcome",
    page_icon="👋",
    layout="wide"
)
import os
from modules.component import info_sidebar
from modules.llm import MODELS, LLM
from modules.utils import get_project_dict, middle_element, PROJECT_PATH
from modules.scenario import ScenarioTree

# initialize session state
session_state_init = {'project': None, 'llm': None, 'data_file': None, 'data_description': None, 'project_path': PROJECT_PATH, 'scenario_tree': ScenarioTree(None), 'scenario_output': None, 'selected_items_dict': {}}
for key, value in session_state_init.items():
    if key not in st.session_state:
        st.session_state[key] = value

st.title('Welcome to Empirical Research Assistant!👋')

projects_dict = get_project_dict()

@st.experimental_dialog("Create a new project")
def create_project():
    new_project_name = st.text_input("Project name:")
    if st.button("Submit"):
        if not os.path.exists(st.session_state.project_path + new_project_name):
            os.makedirs(st.session_state.project_path + new_project_name)
            st.success(f"Project '{new_project_name}' created successfully!")
        else:
            st.error(f"Project '{new_project_name}' already exists!") 
        
st.subheader("Create or Load a Project to Get Started!")

# col11, col12, col13 = st.columns([6,1,1])
col1, col2, col3 = st.columns([6,1,1])

with col1:
    selected_project = st.selectbox(
        "Select a project:",
        list(projects_dict.keys()),
        label_visibility='collapsed',
        index=None,
        placeholder='Select a project'
    )
    
with col2:
    if st.button("Load Project", type='primary', use_container_width=True):
        st.session_state.project = projects_dict[selected_project]
        
with col3:
    if st.button("Create Project", type='primary', use_container_width=True):
        create_project()

st.divider()    

st.subheader("Settings")
openai_api_key = st.text_input("OpenAI API Key", type="password")
with st.expander("Advanced Settings"):
    # set model name with MODELS
    model_name = st.selectbox("Model Name", MODELS, index=0)
    # set temperature with slider
    temperature = st.slider("Temperature", min_value=0.0, max_value=1.0, step=0.1, value=0.7)
    # set openai api base
    openai_api_base = st.text_input("OpenAI API Base", value=None, placeholder="No need to change this unless you are using a custom OpenAI API base.")

col2 = middle_element([6,1,1], 3)
with col2:
    if st.button("Save Settings", type='primary', use_container_width=True):
        llm = LLM(api_key=openai_api_key, temperature=temperature, model_name=model_name, openai_api_base=openai_api_base)
        if llm.test_available():
            st.session_state.llm = llm

info_sidebar()
    
    


               

