import streamlit as st
st.set_page_config(
    page_title="Scenario",
    page_icon="👋",
    layout="wide"
)
from streamlit_react_flow import react_flow
from hashlib import md5
from modules.component import info_sidebar, scenario_selector, scenario_data
from modules.utils import get_selected_items_dict, middle_element

st.title('Scenario')
info_sidebar()
tree = st.session_state.scenario_tree
st.subheader("Scenario Bracnches")
# 图：等待实现
scenario_selector(tree)
st.divider()

st.subheader("Scenario Data")
scenario_data()
st.divider()
    
st.subheader("Scenario Information")
with st.container(border=True):
    st.markdown("### {}\n".format(st.session_state.current_scenario.id)+st.session_state.current_scenario.description)  
with st.expander("Modify Scenario", expanded=True):
    items_option = [f"{name}: {col}" for name, df in st.session_state.data_file.items() for col in df.columns]
    defaults = ["{}: {}".format(k, i['name']) for k, v in st.session_state.current_branch.selected_items.items() for i in v]
    current_selected_items = st.multiselect("Select Data Items", items_option, default=defaults, placeholder="Select Data Items", label_visibility='collapsed')
    current_selected_items_dict = get_selected_items_dict(current_selected_items)

    scenario_name = st.text_input("Scenario Name", st.session_state.current_scenario.id)
    scenario_description = st.text_area("Scenario Description", st.session_state.current_scenario.description, height=300)
    col1, col2, col3, col4 = st.columns([2,1,1,2])
    with col2:
        if st.button("Save as New Scenario", type='primary', use_container_width=True):
            branch_id = md5(str(current_selected_items_dict).encode()).hexdigest()
            tree.add_scenario(branch_id, scenario_name, scenario_description, current_selected_items_dict)
            st.session_state.current_scenario = tree.get_branch(branch_id).get_scenario_by_id(scenario_name)
    with col3:
        if current_selected_items==defaults:
            if st.button("Update Scenario", type='primary', use_container_width=True):
                st.session_state.current_scenario.id = scenario_name
                st.session_state.current_scenario.description = scenario_description
        else:
            st.button("Update Scenario", type='primary', key="us2", use_container_width=True, disabled=True)
st.divider()

col2 = middle_element([2,1,2])
with col2:
    if st.button("Generate Hypothesis", use_container_width=True, type='primary'):
        st.error("Sorry, this feature is not available yet.", icon="🥹")



st.write(st.session_state)

# from streamlit_react_flow import react_flow

# with st.container(border=True):
#     st.subheader("Friends Graph")
#     elements = [
#         { "id": '1', "data": { "label": 'Guru'  }, "type":"input","style": { "background": '#ffcc50', "width": 100 },
#             "position": { "x": 100, "y": 100 } },
#         { "id": '2', "data": { "label": 'Achyuth' },"position": { "x": 300, "y": 100 }},
#         { "id": 'e1-2', "source": '1', "target": '2', "animated": True },
#     ]
#     elements.extend([{"id":i+3,"data":{"label":name },"type":"output","position": { "x": 170*i, "y": 300+i }} for i,name in enumerate(["Aravind","Manoj","Velmurugan","sridhar"])])
#     elements.extend([{"id":f"e{i}-{j}","source":i,"target":j} for i,j in [(1,3),(1,4),(1,5),(1,6)]])
#     flowStyles = { "height": 500,"width":1100 }

#     react_flow("friends",elements=elements,flow_styles=flowStyles)

# def format_branch(branches):
#     res = []
#     for b in branches:
#         selected_items = ["{}: {}".format(k, i['name']) for k, v in b.selected_items.items() for i in v]
#         res.append(", ".join(selected_items))
#     return res