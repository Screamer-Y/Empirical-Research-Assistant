from streamlit_agraph import agraph, Node, Edge, Config

# 创建节点列表
nodes = []
nodes.append(Node(id="Root", label="Root", size=30))
nodes.append(Node(id="Branch1_Node1", label="Branch1_Node1", size=25))
nodes.append(Node(id="Branch1_Node2", label="Branch1_Node2", size=25))
nodes.append(Node(id="Branch2_Node1", label="Branch2_Node1", size=25))
nodes.append(Node(id="Branch2_Node2", label="Branch2_Node2", size=25))
nodes.append(Node(id="Branch2_Node3", label="Branch2_Node3", size=25))
nodes.append(Node(id="Branch3_Node1", label="Branch3_Node1", size=25))
nodes.append(Node(id="Branch3_Node2", label="Branch3_Node2", size=25))

# 创建边列表
edges = []
edges.append(Edge(source="Root", target="Branch1_Node1"))
edges.append(Edge(source="Branch1_Node1", target="Branch1_Node2"))
edges.append(Edge(source="Root", target="Branch2_Node1"))
edges.append(Edge(source="Branch2_Node1", target="Branch2_Node2"))
edges.append(Edge(source="Branch2_Node2", target="Branch2_Node3"))
edges.append(Edge(source="Root", target="Branch3_Node1"))
edges.append(Edge(source="Branch3_Node1", target="Branch3_Node2"))

config = Config(width=1000,
                height=500,
                directed=True, 
                physics=False, 
                hierarchical=True,
                direction='LR',
                sortMethod='directed',
                # **kwargs
                )