from streamlit_agraph import agraph, Node, Edge, Config
import pandas as pd

class AGraph:
    def __init__(self, node_df: pd.DataFrame=None, edge_df: pd.DataFrame=None):
        self.nodes = []
        self.edges = []
        if node_df:
            for row in node_df.iterrows():
                self.nodes.append(Node(row['id'], label=row['label'], title=row['title']))
        if edge_df:
            for row in edge_df.iterrows():
                self.edges.append(Edge(row['source'], row['target'], label=row['label']))
        self.config = Config(width=500,
                height=550,
                directed=True, 
                physics=True, 
                hierarchical=False,
                solver='forceAtlas2Based',
                )
    
    def add_node(self, node: Node):
        self.nodes.append(node)
        
    def add_edge(self, edge: Edge):
        self.edges.append(edge)
        
    def set_config(self, config: Config):
        self.config = config
    
    def render(self):
        return agraph(self.nodes, self.edges, self.config)
    