import streamlit as st
import pandas as pd
import os

PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+ "\\projects\\"
@st.cache_data
def convert_df(df):
    return df.to_csv().encode("utf-8")
NODE_RELATIONSHIP_TEMPLATE = convert_df(pd.read_csv(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+ "\\src\\data_relationship_node_template.csv"))
EDGE_RELATIONSHIP_TEMPLATE = convert_df(pd.read_csv(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+ "\\src\\data_relationship_edge_template.csv"))


def get_project_dict():
    path = PROJECT_PATH
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
    
        