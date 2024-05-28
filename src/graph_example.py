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
    

# class Node:
#   def __init__(self,
#               id,
#               title=None, # displayed if hovered
#               label=None, # displayed inside the node
#               color=None,
#               shape="dot",
#               size=25,
#               **kwargs
#                ):
#       pass

# for edges is source, taget, label

# nodes.append( Node(id="Node1", 
#                    label="Node1", 
#                    size=25)
#             ) 
# nodes.append( Node(id="Node2", 
#                    label="Node2",
#                    size=25) 
#             )
# nodes.append( Node(id="Node3", 
#                    label="Node3",
#                    size=25) 
#             )
# nodes.append( Node(id="Node4", 
#                    label="Node4",
#                    size=25) 
#             )
# nodes.append( Node(id="Node5",
#                      label="Node5",
#                      size=25)
#                 )
# nodes.append( Node(id="Node6",
#                      label="Node6",
#                      size=25)
#                 )

# edges.append( Edge(source="Node1", 
#                    target="Node2",
#                    ) 
#             ) 
# edges.append( Edge(source="Node2",
#                      target="Node3")
#                 )
# edges.append( Edge(source="Node3",
#                      target="Node4")
#                 )
# edges.append( Edge(source="Node4",
#                      target="Node5")
#                 )
# edges.append( Edge(source="Node5",
#                      target="Node6")
#                 )
# edges.append( Edge(source="Node6",
#                         target="Node1")
#                     )
# edges.append( Edge(source="Node1",
#                         target="Node3")
#                     )
# edges.append( Edge(source="Node2",
#                         target="Node4")
#                     )   
# edges.append( Edge(source="Node3",
#                         target="Node5")
#                     )   
# edges.append( Edge(source="Node4",
#                         target="Node6")
#                     )   
# edges.append( Edge(source="Node5",
#                         target="Node1")
#                     )   

config = Config(width=500,
                height=550,
                directed=True, 
                physics=True, 
                hierarchical=False,
                solver='forceAtlas2Based',
                # **kwargs
                )