from streamlit_agraph import agraph, Node, Edge, Config

nodes = []
edges = []
nodes.append( Node(id="Node1", 
                   label="Node1", 
                   size=25)
            ) 
nodes.append( Node(id="Node2", 
                   label="Node2",
                   size=25) 
            )
nodes.append( Node(id="Node3", 
                   label="Node3",
                   size=25) 
            )
nodes.append( Node(id="Node4", 
                   label="Node4",
                   size=25) 
            )
nodes.append( Node(id="Node5",
                     label="Node5",
                     size=25)
                )
nodes.append( Node(id="Node6",
                     label="Node6",
                     size=25)
                )

edges.append( Edge(source="Node1", 
                   target="Node2",
                   ) 
            ) 
edges.append( Edge(source="Node2",
                     target="Node3")
                )
edges.append( Edge(source="Node3",
                     target="Node4")
                )
edges.append( Edge(source="Node4",
                     target="Node5")
                )
edges.append( Edge(source="Node5",
                     target="Node6")
                )
edges.append( Edge(source="Node6",
                        target="Node1")
                    )
edges.append( Edge(source="Node1",
                        target="Node3")
                    )
edges.append( Edge(source="Node2",
                        target="Node4")
                    )   
edges.append( Edge(source="Node3",
                        target="Node5")
                    )   
edges.append( Edge(source="Node4",
                        target="Node6")
                    )   
edges.append( Edge(source="Node5",
                        target="Node1")
                    )   

config = Config(width=750,
                height=500,
                directed=True, 
                physics=True, 
                hierarchical=False,
                # **kwargs
                )