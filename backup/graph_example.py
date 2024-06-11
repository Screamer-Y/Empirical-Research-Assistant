from streamlit_agraph import agraph, Node, Edge, Config
import pandas as pd

nodes = []
edges = []

nodes_df = pd.read_csv(r"C:\Vscode WorkSpace\Empirical-Research-Assistant\src\test_nodes.csv")
edges_df = pd.read_csv(r"C:\Vscode WorkSpace\Empirical-Research-Assistant\src\test_relationships.csv")
# specific id, title and label for nodes
nodes_df.rename(columns={'_id': 'id', 'name': 'label', '_labels':'title'}, inplace=True)
edges_df.rename(columns={'_start': 'source', '_end': 'target', '_type':'label'}, inplace=True)

for index, row in nodes_df.iterrows():
    nodes.append(Node(row['id'], label=row['label'], title=row['title']))

for index, row in edges_df.iterrows():
    edges.append(Edge(row['source'], row['target'], label=row['label']))
    

config = Config(width=500,
                height=550,
                directed=True, 
                physics=True, 
                hierarchical=False,
                solver='forceAtlas2Based',
                # **kwargs
                )