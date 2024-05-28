'''Welcome/Project/Settings'''
import streamlit as st
import os
import time

project_path = os.getcwd() + "\\projects\\"
exisiting_projects = os.listdir(project_path)
if 'openai_api_key' not in st.session_state:
    st.session_state.openai_api_key = ''

st.set_page_config(
    page_title="Welcome",
    page_icon="👋",
    layout="wide"
)

st.title('Welcome to Empirical Research Assistant!👋')

@st.experimental_dialog("Create a new project")
def create_project():
    new_project_name = st.text_input("Project name:")
    if st.button("Submit"):
        if not os.path.exists(project_path + new_project_name):
            os.makedirs(project_path + new_project_name)
            st.success(f"Project '{new_project_name}' created successfully!")
        else:
            st.error(f"Project '{new_project_name}' already exists!") 
        
st.header("Create or Load a Project to Get Started!")
st.write("The working directory is: ", project_path)
st.session_state.project = st.selectbox(
    "Select a project:",
    exisiting_projects)
st.write("Now the project is: ", st.session_state.project)
if st.button("Create New Project"):
    create_project()

st.divider()    

st.header("Settings")
openai_api_key = st.text_input("OpenAI API Key", type="password")
if st.button("Save"):
    st.session_state.openai_api_key = openai_api_key
st.write("OpenAI API Key: ", st.session_state.openai_api_key)
if not st.session_state.openai_api_key.startswith('sk-'):
    st.warning("Please enter your OpenAI API key to enable AI features.", icon="⚠")

               

