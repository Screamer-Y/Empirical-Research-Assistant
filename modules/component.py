import streamlit as st
import os
import pandas as pd
from modules.utils import NODE_RELATIONSHIP_TEMPLATE, EDGE_RELATIONSHIP_TEMPLATE

## Sidebar components
def info_sidebar():
    if st.session_state.get('project'):
        st.sidebar.success("Project '{}' loaded successfully!".format(st.session_state.project.split('\\')[-1]))
    else:
        st.sidebar.error("No project selected.")
        
    if st.session_state.get('llm'):
        st.sidebar.success("LLM has been set up successfully!")
    else:
        st.sidebar.warning("LLM unavailable. Check your settings.")
        
def data_sidebar():
    if st.session_state.get('project'):
        if st.session_state.get('data_file'):
            st.sidebar.success("Data loaded successfully!")
        else:
            st.sidebar.warning("No data loaded yet.")

## Data Page components
def data_file_selector():
    if not st.session_state.get('project'):
        st.error("No project selected. Please select a project first.", icon="🚫")
        return
    project_path = st.session_state.project + '\\data\\'
    data_csv = {name:os.path.join(project_path, name) for name in os.listdir(project_path) if os.path.join(project_path, name).endswith(".csv")}
    names = list(data_csv.keys())
    st.subheader("Select data file(s)")
    col1, col2 = st.columns([7, 1])
    with col1:
        name = st.multiselect(
            "Select data files:",
            names,
            label_visibility='collapsed'
        )
    with col2:
        confirm_button = st.button("Confirm", use_container_width=True, type='primary')
    if confirm_button and name:
        st.session_state.data_file = {}
        st.session_state.data_description = {}
        progress_text = "Loading Data..."
        for n in name:
            my_bar = st.progress(0, text=progress_text)
            chunk_size, chunk_list = 1, []
            total_lines = sum(1 for line in open(data_csv[n], encoding='utf-8')) - 1
            for chunk in pd.read_csv(data_csv[n], chunksize=chunk_size, encoding='utf-8'):
                chunk_list.append(chunk)
                my_bar.progress(len(chunk_list)/total_lines, text=progress_text)
            my_bar.empty()
            df = pd.concat(chunk_list)
            st.session_state.data_file[n] = df
            st.session_state.data_description[n] = pd.DataFrame({'name': df.columns, 'type': [str(t) for t in df.dtypes.tolist()], 'description': [''] * len(df.columns), 'example': [df.iloc[0,i] for i in range(len(df.columns))]}, index=range(1, len(df.columns) + 1))
        st.session_state.scenario_tree.data = st.session_state.data_file
    st.divider()

## Scenario Page components
def scenario_selector(tree):
    col1, col2, col3 = st.columns([3,3,1])
    with col1:
        st.write("Select a branch:")
    with col2:
        st.write("Select a scenario:")
    col1, col2, col3 = st.columns([3,3,1])

    with col1:
        sp_current_branch = st.selectbox("Branch", list(tree.branches.keys()), label_visibility='collapsed')
    with col2:
        sp_current_scenario = st.selectbox("Scenario", [s.id for s in tree.get_branch(sp_current_branch).scenarios], label_visibility='collapsed')
    with col3:
        if st.button("Confirm", type='primary', use_container_width=True):
            st.session_state.current_scenario = tree.get_branch(sp_current_branch).get_scenario_by_id(sp_current_scenario)


def scenario_data():
    for k, v in st.session_state.selected_items_dict.items():
        cols = [i['name'] for i in v]
        df = st.session_state.data_description[k]
        selected_df = df.loc[df['name'].isin(cols)]
        with st.expander(k, expanded=False):
            st.data_editor(selected_df, use_container_width=True)

# 计算重合度并连接场景
from streamlit_agraph import agraph, Node, Edge, Config

## 计算场景相似度
def compute_overlap(selected_items_a, selected_items_b):
    overlap_count = 0
    total_count = 0
    for dataset in selected_items_a:
        if dataset in selected_items_b:
            items_a = selected_items_a[dataset]
            items_b = selected_items_b[dataset]
            names_a = set(item['name'] for item in items_a)
            names_b = set(item['name'] for item in items_b)
            overlap_count += len(names_a.intersection(names_b))
            total_count += len(names_a.union(names_b))
    return overlap_count / total_count if total_count > 0 else 0

## 生成场景流程图
def scenario_graph(tree):
    nodes_list = []
    edges_list = []
    node_id = 1
    branch_counter = 1
    node_dict = {}
    branches_info = []
    max_branch_counter = 0
    candidate_leaf_node_id = None

    # 维护一个映射，用于存储场景ID到节点ID的映射
    scenario_id_to_node_id = {}

    for branch_name, branch in tree.branches.items():
        branch_label = f"Scene Set {branch_counter}"
        branch_node_id = node_id
        nodes_list.append(Node(id=branch_node_id, label=branch_label, level=0, color="lightgreen", border="3px solid green"))
        node_dict[branch_name] = branch_node_id
        node_id += 1

        for scenario in branch.scenarios:
            scenario_node_id = node_id
            nodes_list.append(Node(id=scenario_node_id, label=scenario.id, level=1))  # 其他节点的层级设置为1
            scenario_id_to_node_id[scenario.id] = scenario_node_id
            node_id += 1

        branches_info.append((branch_node_id, branch_name, branch.selected_items, branch_counter))
        branch_counter += 1

    # 使用 scenarios_relation 信息构建边
    for branch_name, branch in tree.branches.items():
        for source, target, relation in branch.scenarios_relation:
            source_node_id = scenario_id_to_node_id[source]
            target_node_id = scenario_id_to_node_id[target]
            edges_list.append(Edge(source=source_node_id, target=target_node_id))

    # 添加额外的边缘
    last_branch_id, last_branch_name, last_selected_items, _ = branches_info[-1]
    if len(tree.get_branch(last_branch_name).scenarios) == 1:
        max_overlap_ratio = 0.7
        for branch_node_id, branch_name, selected_items, current_branch_counter in branches_info[:-1]:
            overlap_ratio = compute_overlap(selected_items, last_selected_items)
            if overlap_ratio > max_overlap_ratio:
                max_overlap_ratio = overlap_ratio
                if current_branch_counter > max_branch_counter:
                    max_branch_counter = current_branch_counter
                    candidate_leaf_node_id = branch_node_id

        if candidate_leaf_node_id:
            tree.add_extra_edge(candidate_leaf_node_id, last_branch_id)

    for source_id, target_id in tree.get_extra_edges():
        edges_list.append(Edge(source=source_id, target=target_node_id, color="red", dashes=True))

    config = Config(width="100%", height=600, directed=True, physics=False, hierarchical=True, layout={'hierarchical': {'direction': 'LR'}})  # 设置图的方向为从左到右
    return agraph(nodes=nodes_list, edges=edges_list, config=config)





