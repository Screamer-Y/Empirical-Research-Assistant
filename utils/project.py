import streamlit as st
import os

def get_project_dict():
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+ "\\projects"
    projects = {name:os.path.join(path, name) for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))}
    return projects
