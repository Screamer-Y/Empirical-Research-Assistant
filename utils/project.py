import streamlit as st
import os

def get_project_dict():
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+ "\\projects"
    projects = {name:os.path.join(path, name) for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))}
    return projects

def middle_element(ratio, index=2):
    col1, col2, col3 = st.columns(ratio)
    if index == 1:
        return col1
    elif index == 2:
        return col2
    elif index == 3:
        return col3
    else:
        return col2
