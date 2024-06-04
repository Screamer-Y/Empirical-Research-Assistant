import streamlit as st
import os
from utils.project import get_project_dict
import time

# initialize session state
session_state_keys = ['project', 'openai_api_key']
for key in session_state_keys:
    if key not in st.session_state:
        st.session_state[key] = None
st.session_state.project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+ "\\projects\\"    

st.set_page_config(
    page_title="Welcome",
    page_icon="👋",
    layout="wide"
)
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

col11, col12, col13 = st.columns([6,1,1])

with col11:
    selected_project = st.selectbox(
        "Select a project:",
        list(projects_dict.keys()),
        label_visibility='collapsed',
        index=None,
        placeholder='Select a project'
    )
    
with col12:
    if st.button("Load Project", type='primary', use_container_width=True):
        st.session_state.project = projects_dict[selected_project]
        
with col13:
    if st.button("Create Project", type='primary', use_container_width=True):
        create_project()

if st.session_state.project:
    st.success("Project '{}' loaded successfully!".format(st.session_state.project.split('\\')[-1]))
st.divider()    

st.subheader("Settings")
col21, col22 = st.columns([7,1])
with col21:
    openai_api_key = st.text_input("OpenAI API Key", type="password", label_visibility='collapsed')
with col22:
    if st.button("Confirm", type='primary', use_container_width=True):
        st.session_state.openai_api_key = openai_api_key

if not st.session_state.openai_api_key or not st.session_state.openai_api_key.startswith('sk-'):
    st.warning("Please enter your OpenAI API key to enable llm generation features.", icon="⚠")
else:
    st.success("OpenAI API key has been set successfully!")

               

