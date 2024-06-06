import streamlit as st
from streamlit_agraph import agraph
import pandas as pd
import numpy as np

import sys
import os
sys.path.append("C:\\Vscode WorkSpace\\Empirical-Research-Assistant\\src")
from src.flow_chat import nodes, edges, config


st.title('Scenario')

st.subheader("Scenario Bracnches:")
with st.container(border=True):
    return_value = agraph(nodes=nodes, 
                        edges=edges, 
                        config=config)

st.subheader("Scenario Description:")
with st.container(border=True):
    st.markdown('''
## Research Scenario: Pattern Analysis and Categorization

### Introduction

In this study, we aim to analyze and categorize various patterns based on their types, descriptions, color palettes, and dimensions. The primary objective is to understand the visual characteristics and thematic elements of different pattern categories, which include geometric, floral, and abstract patterns.

### Pattern Categories

1. **Geometric Patterns**
   - **Description**: Patterns characterized by shapes and forms that follow mathematical rules and symmetry. Common shapes include circles, squares, triangles, and lines.
   - **Color Palette**: Blue, Green, White
   - **Dimensions**: 10x10 inches

2. **Floral Patterns**
   - **Description**: Patterns inspired by natural elements, particularly flowers and foliage. These designs often incorporate curves and organic shapes.
   - **Color Palette**: Red, Yellow, Pink
   - **Dimensions**: 12x12 inches

3. **Abstract Patterns**
   - **Description**: Patterns that do not represent recognizable objects or scenes. They often focus on the use of colors, shapes, and textures to create visual interest.
   - **Color Palette**: Black, White, Red
   - **Dimensions**: 8x8 inches

### Research Objectives

- **Visual Characteristics Analysis**: Examine the visual elements of each pattern category to identify common traits and distinguishing features.
- **Color Palette Study**: Analyze the impact of different color combinations within each pattern type on visual perception and aesthetic appeal.
- **Dimensional Impact**: Investigate how the dimensions of a pattern influence its overall design and viewer perception.

### Methodology

1. **Data Collection**: Gather a dataset of patterns, each tagged with relevant metadata including pattern type, description, color palette, and dimensions.
2. **Qualitative Analysis**: Conduct a detailed visual analysis of patterns within each category to identify common motifs and design principles.
3. **Quantitative Analysis**: Use statistical methods to analyze the frequency and distribution of colors and shapes in each pattern type.
4. **Comparative Study**: Compare the patterns across different categories to identify unique and overlapping characteristics.

### Expected Outcomes

- A comprehensive understanding of the design principles and visual characteristics unique to geometric, floral, and abstract patterns.
- Insights into how color palettes and dimensions contribute to the aesthetic and functional aspects of pattern design.
- Recommendations for designers on how to effectively utilize different pattern types in various applications, such as textiles, graphic design, and interior decor.

### Conclusion

This research will provide valuable insights into the art and science of pattern design, helping to enhance the creative processes of designers and artists across various industries. By systematically analyzing and categorizing patterns, we aim to contribute to the broader field of design studies and visual arts.
''')

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
items = items.iloc[2:6]

st.dataframe(items, use_container_width=True)


df = pd.read_csv(r"C:\Vscode WorkSpace\Empirical-Research-Assistant\projects\test\example_dataset.csv")
df = df[['PatternType', 'Description', 'ColorPalette', 'Dimensions']]
st.subheader("Data Example:")
st.dataframe(df.head(),  use_container_width=True)



st.button("Generate Hypothesis")


