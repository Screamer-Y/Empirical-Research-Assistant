import streamlit as st

st.set_page_config(
    page_title="Welcome",
    page_icon="👋",
    layout="wide"
)

st.title('Welcome to Empirical Research Assistant!👋')

st.header("Create or Load a Project to Get Started!")

if st.button("Create New Project"):
    # Create a popup to ask the user for the project name
    project_name = st.text_input("Enter the project name", "Enter to confirm")
    if project_name:
        pass

if st.button("Select Project from Directory"):
    # Popup to ask the user to select a project from the directory
    pass
    

# st.sidebar.success("Select a demo above.")