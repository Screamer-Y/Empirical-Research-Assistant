import streamlit as st
import pandas as pd
from streamlit_agraph import agraph, Node, Edge, Config

    
import pandas as pd

# 定义节点
nodes = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'label': [
        'Geometric_Patterns',
        'Floral_Patterns',
        'Abstract_Patterns',
        'Color_Consistency',
        'Pattern_Dimensions',
        'Warmer_Color_Palette'
    ]
})

# 定义边
edges = pd.DataFrame({
    'source': [1, 2, 3, 5, 6],
    'target': [4, 4, 4, 1, 2],
    'label': [
        'Higher_Consistency',
        'Higher_Consistency',
        'Higher_Consistency',
        'More_Likely',
        'More_Likely'
    ]
})

col1, col2 = st.columns(2)

with col1:
        st.markdown('''### Hypothesis 1: Geometric patterns have a higher consistency in color usage compared to floral and abstract patterns.''')
        st.markdown('''### Hypothesis 2: Patterns with larger dimensions are more likely to be geometric.''')
        st.markdown('''### Hypothesis 3: Patterns with warmer color palettes (including red and yellow) are more likely to be floral.''')
        nodes_list = []
        edges_list = []
        for index, row in nodes.iterrows():
                nodes_list.append(Node(row['id'], label=row['label']))
        for index, row in edges.iterrows():
                edges_list.append(Edge(row['source'], row['target'], label=row['label']))
        config = Config(width=500,
                height=550,
                directed=True, 
                physics=True, 
                hierarchical=False,
                solver='forceAtlas2Based',
                # **kwargs
                )
        return_value = agraph(nodes=nodes_list, 
                            edges=edges_list, 
                            config=config)

with col2:
        st.code('''
        * Load the data
import excel "pattern_data.xlsx", sheet("Sheet1") firstrow clear

* Generate dummy variables for each pattern type
gen geometric = (PatternType == "geometric")
gen floral = (PatternType == "floral")
gen abstract = (PatternType == "abstract")

* Create a measure for color consistency (e.g., number of unique colors used)
* Assuming ColorPalette is a string of comma-separated colors
egen num_colors = rownonmiss(ColorPalette), strok

* Compare the average number of colors used across pattern types
regress num_colors geometric floral abstract
''')



        st.code('''
        * Load the data
import excel "pattern_data.xlsx", sheet("Sheet1") firstrow clear

* Convert Dimensions to numeric values (assuming they are in the format 'widthxheight')
gen width = real(substr(Dimensions, 1, strpos(Dimensions, "x") - 1))
gen height = real(substr(Dimensions, strpos(Dimensions, "x") + 1, .))

* Calculate the area of each pattern
gen area = width * height

* Generate dummy variables for each pattern type
gen geometric = (PatternType == "geometric")
gen floral = (PatternType == "floral")
gen abstract = (PatternType == "abstract")

* Compare the average area across pattern types
regress area geometric floral abstract
''')



        st.code('''
        * Load the data
import excel "pattern_data.xlsx", sheet("Sheet1") firstrow clear

* Create dummy variables for the presence of specific colors
gen red_present = strpos(ColorPalette, "red") > 0
gen yellow_present = strpos(ColorPalette, "yellow") > 0

* Generate a dummy variable for warm color palettes
gen warm_palette = red_present | yellow_present

* Generate dummy variables for each pattern type
gen geometric = (PatternType == "geometric")
gen floral = (PatternType == "floral")
gen abstract = (PatternType == "abstract")

* Compare the likelihood of having a warm palette across pattern types
logit warm_palette geometric floral abstract
''')
            