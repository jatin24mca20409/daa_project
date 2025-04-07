
import matplotlib.pyplot as plt
import networkx as nx
from graph import graph

def draw_graph(graph_data):
    G = nx.DiGraph()

    for node in graph_data:
        for neighbor, weight in graph_data[node]:
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G)  

    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=14, font_weight='bold')

    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=12)

    plt.title("Smart City Graph - Delivery Routes", fontsize=16)
    plt.show()

draw_graph(graph)
