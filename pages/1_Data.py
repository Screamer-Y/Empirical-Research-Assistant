import streamlit as st
from streamlit_agraph import agraph
import pandas as pd
import numpy as np

import sys
import os
sys.path.append("C:\\Vscode WorkSpace\\Empirical-Research-Assistant\\src")
from src.graph_example import nodes, edges, config

st.set_page_config(
    page_title="Data",
    page_icon="👋",
    layout="wide"
)

with st.container():
    st.title('Data Exploration')
    st.subheader("Data Information:")
    data_items = [
        {"Name": "PatternID", "Type": "Integer", "Description": "A unique identifier for each pattern entry in the dataset."},
        {"Name": "PatternName", "Type": "String", "Description": "The name of the pattern, providing a human-readable reference."},
        {"Name": "PatternType", "Type": "String", "Description": "The category or type of the pattern, such as 'geometric,' 'floral,' or 'abstract.'"},
        {"Name": "Description", "Type": "String", "Description": "A detailed description of the pattern, including its visual characteristics and any notable features."},
        {"Name": "ColorPalette", "Type": "String", "Description": "The primary colors used in the pattern, listed in a comma-separated format."},
        {"Name": "Dimensions", "Type": "String", "Description": "The dimensions of the pattern, usually provided in width x height format (e.g., '10x10 inches')."},
        {"Name": "Resolution", "Type": "Integer", "Description": "The resolution of the pattern image, typically measured in DPI (dots per inch)."},
        {"Name": "FileFormat", "Type": "String", "Description": "The file format of the pattern image, such as 'JPEG,' 'PNG,' or 'SVG.'"},
        {"Name": "CreationDate", "Type": "Date", "Description": "The date on which the pattern was created or added to the dataset."},
        {"Name": "Creator", "Type": "String", "Description": "The name of the individual or entity that created the pattern."},
        {"Name": "UsageRights", "Type": "String", "Description": "Information about the usage rights or licensing of the pattern, specifying any restrictions on use."},
        {"Name": "PopularityScore", "Type": "Float", "Description": "A numerical score representing the popularity or usage frequency of the pattern, often calculated based on user interactions or downloads."},
        {"Name": "Tags", "Type": "String", "Description": "Keywords or tags associated with the pattern, used for search and categorization purposes."},
        {"Name": "ThumbnailURL", "Type": "String", "Description": "A URL link to a thumbnail image of the pattern for quick preview."},
        {"Name": "SourceURL", "Type": "String", "Description": "A URL link to the source or detailed page of the pattern, where users can access more information or download the pattern."}
    ]

    # Create a DataFrame
    items = pd.DataFrame(data_items)
    st.dataframe(items, use_container_width=True)
    
col1, col2 = st.columns(2)

with col1:
    st.subheader("Data Visualization:")
    with st.container(border=True):
        return_value = agraph(nodes=nodes, 
                            edges=edges, 
                            config=config)

with col2:
    df = pd.read_csv(r"C:\Vscode WorkSpace\Empirical-Research-Assistant\projects\test\example_dataset.csv")
    description = df.describe()
    st.subheader("Data Description:")
    st.dataframe(description, use_container_width=True)
    st.subheader("Data Example:")
    st.dataframe(df.head(),  use_container_width=True)

with st.container():
    selected_items = st.multiselect(
        "Selected Items",
        [i["Name"] for i in data_items])
    # 改一下，给予一个修改prompt的dialog，确认
    st.button("Generate a Scenario")
