import networkx as nx
import matplotlib.pyplot as plt
import graphviz
import pydot

G=nx.DiGraph()
G.add_edges_from([ ('q0', 'q1'),('q1', 'q2'),('q2', 'q3'),('q3', 'q4'),('q4', 'q5'),('q5', 'q6'),('q6', 'q7'),('q7', 'q8'),('q8', 'dead'),('q0', 'dead'),('q1', 'dead'),('q2', 'dead'),('q3', 'dead'),('q4', 'dead'),('q5', 'dead'),('q6', 'dead'),('q7', 'dead'),('q7', 'q4'), ('q7', 'q3')])
fixed_positions = {'q0':(-3,1),'q1':(-2,1),'q2':(-1,1),'q3':(0,1),'q4':(1,1),'q5':(2,1),'q6':(3,1),'q7':(4,1),'q8':(5,1),'q9':(6,1),'dead':(1,0.98),}#dict with two of the positions set
fixed_nodes = fixed_positions.keys()
pos=nx.spring_layout(G,pos=fixed_positions, fixed=fixed_nodes)
nx.draw_networkx_nodes(G, pos, node_size=400, node_color='orange')
nx.draw_networkx_edges(G, pos, edgelist=[('q0', 'q1'),('q1', 'q2'),('q2', 'q3'),('q3', 'q4'),('q4', 'q5'),('q5', 'q6'),('q6', 'q7'),('q7', 'q8'),('q8', 'dead'),('q0', 'dead'),('q1', 'dead'),('q2', 'dead'),('q3', 'dead'),('q4', 'dead'),('q5', 'dead'),('q6', 'dead'),('q7', 'dead')], edge_color='black')
nx.draw_networkx_edges(G, pos, edgelist=[('q7', 'q4'), ('q7', 'q3')], edge_color='black', connectionstyle="arc3,rad=0.3")
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edge_labels(G, pos, {('q0', 'q1'):"IF",('q1', 'q2'):"NUMBER",('q2', 'q3'):"THEN",('q3', 'q4'):"ID",('q4', 'q5'):"ASSIGN",('q5', 'q6'):"NUMBER/ID",('q6', 'q7'):"SEMI-COLON",('q7', 'q8'):"END",('q7', 'q4'):"ID",('q7', 'q3'):"ELSE"}, font_size=8)
plt.show()