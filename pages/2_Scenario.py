import streamlit as st
from streamlit_agraph import agraph
import pandas as pd
import numpy as np

st.title('Scenario')

st.subheader("Scenario Bracnches")

st.write("Example:")
from streamlit_react_flow import react_flow
import streamlit as st

with st.container(border=True):

    st.subheader("Friends Graph")

    elements = [
        { "id": '1', "data": { "label": 'Guru'  }, "type":"input","style": { "background": '#ffcc50', "width": 100 },
            "position": { "x": 100, "y": 100 } },
        { "id": '2', "data": { "label": 'Achyuth' },"position": { "x": 300, "y": 100 }},
        { "id": 'e1-2', "source": '1', "target": '2', "animated": True },
    ]

    elements.extend([{"id":i+3,"data":{"label":name },"type":"output","position": { "x": 170*i, "y": 300+i }} for i,name in enumerate(["Aravind","Manoj","Velmurugan","sridhar"])])
    elements.extend([{"id":f"e{i}-{j}","source":i,"target":j} for i,j in [(1,3),(1,4),(1,5),(1,6)]])
    flowStyles = { "height": 500,"width":1100 }

    # Create an instance of our component with a constant `name` arg, and
    # print its output value.
    react_flow("friends",elements=elements,flow_styles=flowStyles)



st.divider()
st.subheader("Scenario Description")
# st.write(vars(st.session_state.scenario_tree))
# st.write(vars(list(st.session_state.scenario_tree.branches.values())[0].scenarios[0]))
# st.write(st.session_state.selected_items_dict)
st.info("You can modify and save the scenario.", icon="ℹ️")
scenario_str = ''
for key, value in st.session_state.scenario_output.items():
    scenario_str += f"### {key}\n{value}\n"
scenario_str = scenario_str[:-1]
st.text_area("Scenario",scenario_str,height=500,label_visibility='collapsed', )
if st.button("Save Scenario", type='primary'):
    st.success("Scenario saved successfully!")

st.subheader("Data Information:")

# Create a DataFrame
# items = pd.DataFrame(data_items)
# items = items.iloc[2:6]

# st.dataframe(items, use_container_width=True)


# df = pd.read_csv(r"C:\Vscode WorkSpace\Empirical-Research-Assistant\projects\test\example_dataset.csv")
# df = df[['PatternType', 'Description', 'ColorPalette', 'Dimensions']]
# st.subheader("Data Example:")
# st.dataframe(df.head(),  use_container_width=True)



st.button("Generate Hypothesis")


